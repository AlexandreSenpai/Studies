
from dataclasses import dataclass
from src.app.core.interfaces.dto import DTO
from src.app.core.interfaces.session_repository import ISessionRepository
from src.app.core.interfaces.use_case import IUseCase
from src.domain.entities.session import Session

@dataclass
class GetSessionRequest:
    id: str

@dataclass
class GetSessionResponse:
    session: Session

class GetSessionUseCase(IUseCase[GetSessionRequest, GetSessionResponse]):
    def __init__(self,
                 session_repository: ISessionRepository) -> None:
        self.session_repository = session_repository

    async def execute(self, 
                      info: DTO[GetSessionRequest] | None = None) -> DTO[GetSessionResponse]:
        if info is None:
            raise ValueError("info is required")
        
        session = await self.session_repository.find_one(id=info.data.id)
        
        return DTO(data=GetSessionResponse(session=session))