from typing import Annotated
from fastapi import Cookie, Depends, Query, Request, routing
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src.infra.core.interfaces.create_session import CreateSessionRequestBody
from src.infra.core.interfaces.signup import SignUpRequestBody
from src.infra.entrypoints.controllers.get_oauth_config import get_oauth_config_controller
from src.infra.entrypoints.controllers.login import login_controller
from src.infra.entrypoints.controllers.get_token import get_token_controller
from src.infra.entrypoints.controllers.signup import signup_controller
from src.infra.entrypoints.controllers.create_session import create_session_controller
from src.infra.entrypoints.controllers.get_session import get_session_controller

router = routing.APIRouter()
security = HTTPBasic()

@router.get('/oauth/config')
async def config():
    return await get_oauth_config_controller.perform()

@router.post('/oauth/login')
async def login(credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                request: Request):
    return await login_controller.perform(email=credentials.username, 
                                          password=credentials.password,
                                          session_id=request.cookies.get("minorin.session"))

@router.get('/oauth/token')
async def token(code: str = Query(None), 
                code_verifier: str = Query(None)):
    return await get_token_controller.perform(code=code,
                                              code_verifier=code_verifier)

@router.post('/oauth/signup')
async def signup(user: SignUpRequestBody):
    return await signup_controller.perform(email=user.email, 
                                           password=user.password, 
                                           username=user.username)

@router.post('/session')
async def create_session(session_data: CreateSessionRequestBody):
    return await create_session_controller.perform(code_challenge=session_data.code_challenge,
                                                   callback_redirect=session_data.callback_redirect,
                                                   callback_uri=session_data.callback_uri,
                                                   client_id=session_data.client_id,
                                                   code_challenge_method=session_data.code_challenge_method,
                                                   response_type=session_data.response_type,
                                                   scopes=session_data.scopes,
                                                   state=session_data.state)

@router.get('/session')
async def get_session(id: str):
    return await get_session_controller.perform(id=id)