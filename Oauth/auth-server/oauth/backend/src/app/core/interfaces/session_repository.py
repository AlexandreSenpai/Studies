from src.app.core.interfaces.repository import IRepository

from src.domain.entities.session import Session

class ISessionRepository(IRepository[Session]):
    ...