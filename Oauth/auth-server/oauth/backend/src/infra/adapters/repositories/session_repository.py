import json
from src.app.core.handlers.error import DatabaseUnavailable, ResourceNotFound
from src.app.core.interfaces.session_repository import ISessionRepository
from src.domain.entities.session import Session, SessionProps
from src.infra.database.redis import redis

class SessionRepository(ISessionRepository):

    async def create(self, entity: Session) -> bool:
        if redis.client is None: return False
        created: bool = await redis.client.set(entity.id, json.dumps(entity.to_dict()))
        await redis.client.expire(entity.id, 600)
        return created

    async def find_one(self, id: str | int) -> Session:
        if redis.client is None: raise DatabaseUnavailable("Redis is unavailable.")
        
        _bytes: bytes = await redis.client.get(str(id))
        
        if _bytes is None:
            raise ResourceNotFound("Could not find the requested session.")
        
        found: SessionProps = json.loads(_bytes)

        return Session(id=str(found.get('id')),
                       created_at=found.get('created_at'),
                       updated_at=found.get('updated_at'),
                       code_challenge=found.get('code_challenge'),
                       state=found.get('state'),
                       scopes=found.get('scopes'),
                       callback_redirect=found.get('callback_redirect'),
                       callback_uri=found.get('callback_uri'),
                       client_id=found.get('client_id'),
                       code_challenge_method=found.get('code_challenge_method'),
                       response_type=found.get('response_type'))
