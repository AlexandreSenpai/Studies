from pydantic import BaseModel


class SignUpRequestBody(BaseModel):
    username: str
    email: str
    password: str