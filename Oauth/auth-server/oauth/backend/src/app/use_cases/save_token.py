from dataclasses import dataclass
from src.app.core.interfaces.use_case import DTO, IUseCase
from src.infra.adapters.repositories.oauth_repository import OauthRepository
from src.domain.entities.token import Token

@dataclass
class SaveTokenRequest:
  token: Token

@dataclass
class SaveTokenResponse:
  saved: bool

class SaveTokenUseCase(IUseCase[SaveTokenRequest, SaveTokenResponse]):

    def __init__(self, oauth_repository: OauthRepository):
        self.oauth_repository = oauth_repository

    async def execute(self, info: DTO[SaveTokenRequest] | None = None) -> DTO[SaveTokenResponse]:
        if info is None: return DTO(SaveTokenResponse(saved=False))
        await self.oauth_repository.create(info.data.token)
        return DTO(SaveTokenResponse(saved=True))