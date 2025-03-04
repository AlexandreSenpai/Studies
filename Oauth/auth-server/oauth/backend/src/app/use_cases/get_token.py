from dataclasses import dataclass
from src.app.core.interfaces.oauth_repository import IOauthRepository
from src.app.core.interfaces.use_case import DTO, IUseCase
from src.domain.entities.token import Token

@dataclass
class GetTokenRequest:
  code: str

@dataclass
class GetTokenResponse:
  token: Token

class GetTokenUseCase(IUseCase[GetTokenRequest, GetTokenResponse]):

  def __init__(self, oauth_repository: IOauthRepository):
    self.oauth_repository = oauth_repository

  async def execute(self, info: DTO[GetTokenRequest] | None = None) -> DTO[GetTokenResponse]:
    if info is None: 
      raise ValueError("info is required")
    
    token = await self.oauth_repository.find_one(info.data.code)

    if token is None:
      raise ValueError("Token not found")

    return DTO(GetTokenResponse(token=token))