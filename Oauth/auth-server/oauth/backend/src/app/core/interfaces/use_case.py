from abc import ABC, abstractmethod
from src.app.core.interfaces.dto import DTO

class IUseCase[T, V](ABC):
    @abstractmethod
    async def execute(self, info: DTO[T] | None = None) -> DTO[V]:
        ...