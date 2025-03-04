from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Union
from src.domain.entities.base import Entity as BaseEntity

Entity = TypeVar('Entity', bound=BaseEntity)

class IRepository(ABC, Generic[Entity]):
    @abstractmethod
    async def create(self, entity: Entity) -> bool:
        ...

    @abstractmethod
    async def find_one(self, id: Union[str, int]) -> Entity:
        ...