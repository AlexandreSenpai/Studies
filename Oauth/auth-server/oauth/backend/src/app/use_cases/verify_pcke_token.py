import base64
from dataclasses import dataclass
import hashlib
from src.app.core.handlers.error import InvalidResource
from src.app.core.interfaces.use_case import DTO, IUseCase
from src.infra.adapters.repositories.oauth_repository import OauthRepository

@dataclass
class PCKERequest:
  code_challenge: str
  code_verifier: str

@dataclass
class PCKEResponse:
  valid: bool

class VerifyPCKEUseCase(IUseCase[PCKERequest, PCKEResponse]):

    def __init__(self, oauth_repository: OauthRepository):
        self.oauth_repository = oauth_repository

    async def generate_code_challenge(self, code_verifier: str) -> str:
       hash = hashlib.sha256(code_verifier.encode('utf-8')).digest()
       return base64.urlsafe_b64encode(hash).rstrip(b'=').decode('utf-8')

    async def execute(self, info: DTO[PCKERequest] | None = None) -> DTO[PCKEResponse]:
        if info is None:
           raise InvalidResource()

        new_hash = await self.generate_code_challenge(code_verifier=info.data.code_verifier)

        return DTO(
            data=PCKEResponse(
                valid=new_hash == info.data.code_challenge
            )
        )