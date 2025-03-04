from src.app.core.interfaces.dto import DTO
from src.app.core.interfaces.use_case import IUseCase
from src.app.use_cases.get_session import GetSessionRequest, GetSessionResponse, GetSessionUseCase
from src.infra.adapters.repositories.session_repository import SessionRepository


class GetSessionController:
    def __init__(self, 
                 get_session_use_case: IUseCase[GetSessionRequest, GetSessionResponse]) -> None:
        self.get_session_use_case = get_session_use_case

    async def perform(self, id: str):
        response = await self.get_session_use_case.execute(
            info=DTO(
                data=GetSessionRequest(
                    id=id
                )
            )
        )
        return { "session": response.data.session.to_dict() }
    
get_session_controller = GetSessionController(
    get_session_use_case=GetSessionUseCase(
        session_repository=SessionRepository()
    )
)