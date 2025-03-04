from src.app.core.interfaces.dto import DTO
from src.app.core.interfaces.facade import IOrchestrator
from src.app.orchestrators.retrieve_token import RetrieveTokenOrchestrator, RetrieveTokenOrchestratorRequest, RetrieveTokenOrchestratorResponse
from src.app.use_cases.get_token import GetTokenUseCase
from src.app.use_cases.verify_pcke_token import VerifyPCKEUseCase
from src.infra.adapters.repositories.oauth_repository import OauthRepository


class GetTokenController:
    def __init__(self, 
                 get_token_orchestrator: IOrchestrator[RetrieveTokenOrchestratorRequest, RetrieveTokenOrchestratorResponse]) -> None:
        self.get_token_orchestrator = get_token_orchestrator

    async def perform(self, code: str, code_verifier: str):
        response = await self.get_token_orchestrator.compose(
            dto=DTO(
                data=RetrieveTokenOrchestratorRequest(
                    code_verifier=code_verifier,
                    code=code
                )
            )
        )
        return {"access_token": response.data.token.access_token,
                "refresh_token": response.data.token.refresh_token}
    
get_token_controller = GetTokenController(
    get_token_orchestrator=RetrieveTokenOrchestrator(
        get_token_use_case=GetTokenUseCase(
            oauth_repository=OauthRepository()
        ),
        verify_pcke_use_case=VerifyPCKEUseCase(
            oauth_repository=OauthRepository()
        )
    )
)