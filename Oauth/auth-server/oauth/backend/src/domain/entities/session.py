from datetime import datetime
from typing import Optional, TypedDict
from src.domain.entities.base import Entity, PropsWithDefaults

class SessionProps(PropsWithDefaults, TypedDict):
    code_challenge: str
    callback_uri: str
    callback_redirect: str
    scopes: list[str]
    state: str
    response_type: str
    client_id: str
    code_challenge_method: str

class Session(Entity[SessionProps]):
    def __init__(self,
                 code_challenge: str,
                 callback_uri: str,
                 callback_redirect: str,
                 scopes: list[str],
                 state: str,
                 response_type: str,
                 client_id: str,
                 code_challenge_method: str,
                 id: Optional[str] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:
        
        super().__init__(id, created_at, updated_at)

        self.code_challenge: str = code_challenge
        self.callback_uri: str = callback_uri
        self.callback_redirect: str = callback_redirect
        self.scopes: list[str] = scopes
        self.state: str = state
        self.response_type: str = response_type
        self.client_id: str = client_id
        self.code_challenge_method: str = code_challenge_method
