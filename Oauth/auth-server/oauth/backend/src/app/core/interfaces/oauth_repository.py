from src.app.core.interfaces.repository import IRepository
from abc import ABC, abstractmethod

from src.domain.entities.token import Token
from src.infra.database.mongo.models.config import Config

class IOauthRepository(IRepository[Token], ABC):
    @abstractmethod
    async def get_config(self) -> Config | None:
        ...