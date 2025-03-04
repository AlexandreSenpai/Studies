
from dataclasses import dataclass
from src.app.core.interfaces.auth import IAuthProvider
from src.app.core.interfaces.dto import DTO
from src.app.core.interfaces.use_case import IUseCase

@dataclass
class CreateAccountRequest:
    email: str
    username: str
    password: str

@dataclass
class CreateAccountResponse:
    created: bool

class CreateAccountUseCase(IUseCase[CreateAccountRequest, CreateAccountResponse]):
    def __init__(self,
                 auth_provider: IAuthProvider) -> None:
        self.auth_provider = auth_provider

    async def execute(self, 
                      info: DTO[CreateAccountRequest] | None = None) -> DTO[CreateAccountResponse]:
        if info is None:
            raise ValueError("info is required")
        
        await self.auth_provider.signup(email=info.data.email,
                                        username=info.data.username,
                                        password=info.data.password)
        
        return DTO(data=CreateAccountResponse(created=True))