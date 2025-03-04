from dataclasses import dataclass
from src.app.core.interfaces.dto import DTO
from src.app.core.interfaces.session_repository import ISessionRepository
from src.app.core.interfaces.use_case import IUseCase
from src.domain.entities.session import Session

@dataclass
class CreateSessionRequest:
    code_challenge: str
    callback_uri: str
    callback_redirect: str
    scopes: list[str]
    state: str
    response_type: str
    client_id: str
    code_challenge_method: str

@dataclass
class CreateSessionResponse:
    session_id: str

class CreateSessionUseCase(IUseCase[CreateSessionRequest, CreateSessionResponse]):
    def __init__(self,
                 session_repository: ISessionRepository) -> None:
        self.session_repository = session_repository

    async def execute(self, 
                      info: DTO[CreateSessionRequest] | None = None) -> DTO[CreateSessionResponse]:
        if info is None:
            raise ValueError("info is required")
        
        data = info.data
        session = Session(code_challenge=data.code_challenge,
                          callback_redirect=data.callback_redirect,
                          callback_uri=data.callback_uri,
                          client_id=data.client_id,
                          code_challenge_method=data.code_challenge_method,
                          response_type=data.response_type,
                          scopes=data.scopes,
                          state=data.state)

        await self.session_repository.create(session)
        
        return DTO(data=CreateSessionResponse(session_id=session.id))