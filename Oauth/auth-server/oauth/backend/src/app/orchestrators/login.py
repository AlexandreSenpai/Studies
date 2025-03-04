from pydantic import BaseModel
from src.app.core.interfaces.facade import IOrchestrator
from src.app.core.interfaces.use_case import DTO
from src.app.core.interfaces.use_case import IUseCase
from src.app.use_cases.get_session import GetSessionRequest, GetSessionResponse
from src.app.use_cases.login import LoginRequest, LoginResponse
from src.app.use_cases.save_token import SaveTokenRequest, SaveTokenResponse

class LoginOrchestratorRequest(BaseModel):
    email: str
    password: str
    session_id: str

class LoginOrchestratorResponse(BaseModel):
    code: str

class LoginOrchestrator(IOrchestrator[LoginOrchestratorRequest, LoginOrchestratorResponse]):

    def __init__(self, 
                 save_token_use_case: IUseCase[SaveTokenRequest, SaveTokenResponse],
                 login_use_case: IUseCase[LoginRequest, LoginResponse],
                 get_session_use_case: IUseCase[GetSessionRequest, GetSessionResponse]) -> None:
        self.save_token_use_case = save_token_use_case
        self.login_use_case = login_use_case
        self.get_session_use_case = get_session_use_case

    async def compose(self, dto: DTO[LoginOrchestratorRequest] | None = None) -> DTO[LoginOrchestratorResponse]:
        if dto is None or dto.data is None:
            raise ValueError("DTO data is required")
        
        session = await self.get_session_use_case.execute(
            info=DTO(
                data=GetSessionRequest(id=dto.data.session_id)
            )
        )

        token_response = await self.login_use_case.execute(
            info=DTO(
                data=LoginRequest(
                    email=dto.data.email,
                    password=dto.data.password
                )
            )
        )

        token = token_response.data.token
        token.add_code_challenge(code_challenge=session.data.session.code_challenge)

        await self.save_token_use_case.execute(
            info=DTO(
                data=SaveTokenRequest(
                    token=token
                )
            )
        )

        return DTO(data=LoginOrchestratorResponse(code=token.id))