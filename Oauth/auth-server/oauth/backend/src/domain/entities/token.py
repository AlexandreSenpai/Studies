from datetime import datetime
from typing import Optional, TypedDict
from src.domain.entities.base import Entity

class TokenProps(TypedDict):
    code_challenge: str
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str
    issuer: str
    subject: str

class Token(Entity[TokenProps]):
    def __init__(self,
                 token_type: str,
                 expires_in: int,
                 subject: str,
                 code_challenge: Optional[str] = None,
                 access_token: Optional[str] = None,
                 refresh_token: Optional[str] = None,
                 id: Optional[str] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:
        
        super().__init__(id, created_at, updated_at)

        self.access_token: None | str = access_token
        self.refresh_token: None | str = refresh_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.subject = subject
        self.code_challenge = code_challenge

    def add_access_token(self, access_token: str) -> None:
        self.access_token = access_token

    def add_refresh_token(self, refresh_token: str) -> None:
        self.refresh_token = refresh_token

    def add_code_challenge(self, code_challenge: str) -> None:
        self.code_challenge = code_challenge