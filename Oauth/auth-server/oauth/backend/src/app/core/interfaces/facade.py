from abc import ABC, abstractmethod

from src.app.core.interfaces.dto import DTO

class IOrchestrator[T, V](ABC):
    @abstractmethod
    async def compose(self, dto: DTO[T] | None = None) -> DTO[V]:
        ...