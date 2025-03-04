from fastapi import Response
from fastapi.responses import JSONResponse
from src.app.core.interfaces.dto import DTO
from src.app.core.interfaces.use_case import IUseCase
from src.app.use_cases.create_session import CreateSessionRequest, CreateSessionResponse, CreateSessionUseCase
from src.infra.adapters.repositories.session_repository import SessionRepository


class CreateSessionController:
    def __init__(self, 
                 create_session_use_case: IUseCase[CreateSessionRequest, CreateSessionResponse]) -> None:
        self.create_session_use_case = create_session_use_case

    async def perform(self, 
                      code_challenge: str,
                      callback_uri: str,
                      callback_redirect: str,
                      scopes: list[str],
                      state: str,
                      response_type: str,
                      client_id: str,
                      code_challenge_method: str):
        res = await self.create_session_use_case.execute(
            info=DTO(
                data=CreateSessionRequest(
                    code_challenge=code_challenge,
                    callback_uri=callback_uri,
                    callback_redirect=callback_redirect,
                    client_id=client_id,
                    code_challenge_method=code_challenge_method,
                    response_type=response_type,
                    scopes=scopes,
                    state=state
                )
            )
        )

        response = Response(status_code=201)
        response.set_cookie(key='minorin.session', 
                            value=res.data.session_id,
                            max_age=600,
                            samesite="none",
                            domain="minorin.io",
                            httponly=True,
                            secure=True)
        
        return response

create_session_controller = CreateSessionController(
    create_session_use_case=CreateSessionUseCase(
        session_repository=SessionRepository()
    )
)