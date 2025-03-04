from dataclasses import dataclass
from typing import Optional
from src.app.core.interfaces.oauth_repository import IOauthRepository
from src.app.core.interfaces.use_case import DTO, IUseCase

@dataclass
class GetOauthConfigResponse:
  issuer: str
  authorization_endpoint: str
  token_endpoint: str
  revoke_endpoint: str
  certs: str
  response_types_supported: list[str]
  subject_types_supported: list[str]
  id_token_signing_alg_values_supported: list[str]
  scopes_supported: list[str]
  token_endpoint_auth_methods_supported: list[str]
  claims_supported: list[str]
  code_challenge_methods_supported: list[str]
  grant_types_supported: list[str]

class GetOauthConfigUseCase(IUseCase[None, GetOauthConfigResponse]):

    def __init__(self, oauth_repository: IOauthRepository):
        self.oauth_repository = oauth_repository

    async def execute(self, info: Optional[DTO[None]] = None) -> DTO[GetOauthConfigResponse]:
        config = await self.oauth_repository.get_config()

        if config is None:
            raise Exception("Could not get oauth config")
        
        return DTO(GetOauthConfigResponse(issuer=config.issuer,
                                          authorization_endpoint=config.authorization_endpoint,
                                          token_endpoint=config.token_endpoint,
                                          revoke_endpoint=config.revoke_endpoint,
                                          certs=config.certs,
                                          response_types_supported=config.response_types_supported,
                                          subject_types_supported=config.subject_types_supported,
                                          id_token_signing_alg_values_supported=config.id_token_signing_alg_values_supported,
                                          scopes_supported=config.scopes_supported,
                                          token_endpoint_auth_methods_supported=config.token_endpoint_auth_methods_supported,
                                          claims_supported=config.claims_supported,
                                          code_challenge_methods_supported=config.code_challenge_methods_supported,
                                          grant_types_supported=config.grant_types_supported))