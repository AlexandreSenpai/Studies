from fastapi import Response
from fastapi.responses import JSONResponse
from src.app.core.interfaces.dto import DTO
from src.app.core.interfaces.use_case import IUseCase
from src.app.use_cases.create_account import CreateAccountRequest, CreateAccountResponse, CreateAccountUseCase
from src.infra.adapters.auth.firebase_auth import FirebaseAuth

class SignUpController:
    def __init__(self, 
                 signup_use_case: IUseCase[CreateAccountRequest, CreateAccountResponse]) -> None:
        self.signup_use_case = signup_use_case

    async def perform(self, email: str, password: str, username: str):
        response = await self.signup_use_case.execute(
            info=DTO(
                data=CreateAccountRequest(
                    username=username,
                    email=email, 
                    password=password
                )
            )
        )
        return JSONResponse(content={"signedUp": True}, status_code=201)
    
signup_controller = SignUpController(
    signup_use_case=CreateAccountUseCase(
        auth_provider=FirebaseAuth()
    )
)