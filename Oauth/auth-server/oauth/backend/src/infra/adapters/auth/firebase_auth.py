
import asyncio
import os

import firebase_admin
from firebase_admin import auth

import firebase_admin.exceptions
from httpx import AsyncClient

from src.app.core.handlers.error import BadRequest, InvalidCredentials, Unknown
from src.app.core.interfaces.auth import IAuthProvider
from src.app.core.interfaces.firebase_login import FirebaseLoginSuccess
from src.domain.entities.token import Token

class FirebaseAuth(IAuthProvider):

    def __init__(self) -> None:
        self.admin = self.__create_firebase_app()

    def __create_firebase_app(self) -> firebase_admin.App:
        return firebase_admin.initialize_app() if len(firebase_admin._apps.keys()) == 0 else firebase_admin.get_app()

    async def login(self,
                    email: str, 
                    password: str) -> Token:
        async with AsyncClient() as client:
            response = await client.post(url="https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword",
                                         json={"email": email, "password": password, "returnSecureToken": True},
                                         params={"key": os.getenv('FIREBASE_TOKEN')})
    
            if response.status_code != 200:
                raise InvalidCredentials()

            data: FirebaseLoginSuccess = response.json()
            
            token = Token(expires_in=int(data.get('expiresIn')),
                          subject=email,
                          token_type="Bearer")
      
            token.add_access_token(data.get('idToken'))
            token.add_refresh_token(data.get('refreshToken'))

            return token
        
    async def __handle_firebase_errors(self, 
                                       error: firebase_admin.exceptions.FirebaseError) -> None:
        match error.code:
            case 'ALREADY_EXISTS':
                raise BadRequest(message="This email or username is already in use")
            case _:
                raise Unknown() 

    async def signup(self, 
                     email: str, 
                     password: str, 
                     username: str) -> None:
        try:
            response: auth.UserRecord = await asyncio.to_thread(auth.create_user,
                                                                uid=username,
                                                                email=email,
                                                                password=password,
                                                                display_name=username,
                                                                photo_url="https://pbs.twimg.com/media/FMjZST1XwAA269V?format=jpg&name=4096x4096")
            
        except firebase_admin.exceptions.FirebaseError as err:
            await self.__handle_firebase_errors(err)