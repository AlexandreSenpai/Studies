from abc import ABC, abstractmethod
from src.domain.entities.token import Token

class IAuthProvider(ABC):
    @abstractmethod
    async def signup(self, 
                     email: str, 
                     password: str,
                     username: str) -> None:
        ...

    @abstractmethod
    async def login(self,
                    email: str,
                    password: str) -> Token:
        ...