from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

Connection = TypeVar('Connection')
Credentials = TypeVar('Credentials')

class IDatabase(ABC, Generic[Connection, 
                             Credentials]):
    @abstractmethod
    async def connect(self, 
                      credentials: Optional[Credentials] = None) -> Connection:
        ...

    @abstractmethod
    async def disconnect(self) -> bool:
        ...