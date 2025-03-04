from datetime import datetime
from typing import Annotated, Optional
from beanie import Document, Indexed

class Tokens(Document):
    code: Annotated[str, Indexed(key="code", unique=True)]
    created_at: datetime
    updated_at: Annotated[datetime, Indexed(key="updated_at", expireAfterSeconds=86400)]
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    subject: str
    code_challenge: Optional[str] = None

    class Settings:
        name = "tokens"
        use_timesync = True
