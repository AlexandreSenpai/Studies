from src.app.core.handlers.error import DatabaseUnavailable, ResourceNotFound
from src.app.core.interfaces.oauth_repository import IOauthRepository
from src.domain.entities.token import Token
from src.infra.database.mongo.models.config import Config
from src.infra.database.mongo.models.token import Tokens

from src.infra.database.mongo import database

class OauthRepository(IOauthRepository):

    async def get_config(self) -> Config | None:
        if database.client is None: return
        config = await Config.find_one()
        return config
    
    async def create(self, entity: Token) -> bool:
        to_create = Tokens(code=entity.id,
                           code_challenge=entity.code_challenge,
                           created_at=entity.created_at,
                           updated_at=entity.updated_at,
                           access_token=entity.access_token or "",
                           expires_in=entity.expires_in,
                           refresh_token=entity.refresh_token or "",
                           subject=entity.subject,
                           token_type=entity.token_type)
        return await to_create.create() is not None

    async def find_one(self, id: str | int) -> Token:
        
        if database.client is None: raise DatabaseUnavailable()

        token = await Tokens.find_one(Tokens.code == id)
        
        if token is None: raise ResourceNotFound()

        return Token(id=token.code,
                     created_at=token.created_at,
                     updated_at=token.updated_at,
                     code_challenge=token.code_challenge,
                     access_token=token.access_token,
                     expires_in=token.expires_in,
                     refresh_token=token.refresh_token,
                     subject=token.subject,
                     token_type=token.token_type)
