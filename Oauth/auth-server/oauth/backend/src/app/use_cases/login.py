from dataclasses import dataclass

from src.app.core.interfaces.auth import IAuthProvider
from src.app.core.interfaces.use_case import DTO, IUseCase
from src.domain.entities.token import Token

@dataclass
class LoginRequest:
  email: str
  password: str

@dataclass
class LoginResponse:
  token: Token

class LoginUseCase(IUseCase[LoginRequest, LoginResponse]):

  def __init__(self,
               auth_provider: IAuthProvider):
    self.auth_provider = auth_provider

  async def execute(self, info: DTO[LoginRequest] | None = None) -> DTO[LoginResponse]:
    if info is None:
      raise ValueError("info is required")
  
    token = await self.auth_provider.login(email=info.data.email, 
                                           password=info.data.password)
    
    return DTO(data=LoginResponse(token=token))
  
    