from pydantic import BaseModel
from src.app.core.handlers.error import Forbidden, InvalidResource
from src.app.core.interfaces.facade import IOrchestrator
from src.app.core.interfaces.use_case import DTO
from src.app.core.interfaces.use_case import IUseCase
from src.app.use_cases.get_token import GetTokenRequest, GetTokenResponse
from src.app.use_cases.verify_pcke_token import PCKERequest, PCKEResponse
from src.domain.entities.token import Token

class RetrieveTokenOrchestratorRequest(BaseModel):
    code_verifier: str
    code: str

class RetrieveTokenOrchestratorResponse(BaseModel, arbitrary_types_allowed=True):
    token: Token

class RetrieveTokenOrchestrator(IOrchestrator[RetrieveTokenOrchestratorRequest, RetrieveTokenOrchestratorResponse]):

    def __init__(self,
                 get_token_use_case: IUseCase[GetTokenRequest, GetTokenResponse],
                 verify_pcke_use_case: IUseCase[PCKERequest, PCKEResponse]) -> None:
        self.get_token_use_case = get_token_use_case
        self.verify_pcke_use_case = verify_pcke_use_case

    async def compose(self, dto: DTO[RetrieveTokenOrchestratorRequest] | None = None) -> DTO[RetrieveTokenOrchestratorResponse]:
        if dto is None or dto.data is None:
            raise ValueError("DTO data is required")

        token_response = await self.get_token_use_case.execute(
            info=DTO(
                data=GetTokenRequest(
                    code=dto.data.code
                )
            )
        )

        token = token_response.data.token

        if token.code_challenge is None:
            raise InvalidResource("Invalid Code Challenge.")

        valid = await self.verify_pcke_use_case.execute(
            info=DTO(
                data=PCKERequest(
                    code_challenge=token.code_challenge,
                    code_verifier=dto.data.code_verifier
                )
            )
        )

        if not valid:
            raise Forbidden("Access Forbidden Due Invalid Code Verifier.")

        return DTO(data=RetrieveTokenOrchestratorResponse(token=token))