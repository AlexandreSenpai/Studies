
from fastapi.security import HTTPBasic
from src.app.core.handlers.error import InvalidResource
from src.app.core.interfaces.dto import DTO
from src.app.core.interfaces.facade import IOrchestrator
from src.app.orchestrators.login import LoginOrchestrator, LoginOrchestratorRequest, LoginOrchestratorResponse
from src.app.use_cases.get_session import GetSessionUseCase
from src.app.use_cases.login import LoginUseCase
from src.app.use_cases.save_token import SaveTokenUseCase
from src.infra.adapters.auth.firebase_auth import FirebaseAuth
from src.infra.adapters.repositories.oauth_repository import OauthRepository
from src.infra.adapters.repositories.session_repository import SessionRepository

security = HTTPBasic()

class LoginController:
    def __init__(self, 
                 login_orchestrator: IOrchestrator[LoginOrchestratorRequest, LoginOrchestratorResponse]) -> None:
        self.login_orchestrator = login_orchestrator

    async def perform(self, 
                      email: str, 
                      password: str,
                      session_id: str | None):
        
        if session_id is None:
            raise InvalidResource("An invalid session was provided.")

        response = await self.login_orchestrator.compose(
            dto=DTO(
                data=LoginOrchestratorRequest(
                    email=email, 
                    password=password,
                    session_id=session_id
                )
            )
        )
        return { "code": response.data.code }
    
login_controller = LoginController(
    login_orchestrator=LoginOrchestrator(
        save_token_use_case=SaveTokenUseCase(
            oauth_repository=OauthRepository()
        ),
        login_use_case=LoginUseCase(
            auth_provider=FirebaseAuth()
        ),
        get_session_use_case=GetSessionUseCase(
            session_repository=SessionRepository()
        )
    )
)