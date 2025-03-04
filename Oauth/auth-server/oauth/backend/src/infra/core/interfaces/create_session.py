from pydantic import BaseModel


class CreateSessionRequestBody(BaseModel):
    code_challenge: str
    callback_uri: str
    callback_redirect: str
    scopes: list[str]
    state: str
    response_type: str
    client_id: str
    code_challenge_method: str