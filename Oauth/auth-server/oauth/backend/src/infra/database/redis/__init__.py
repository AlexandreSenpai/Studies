
from dataclasses import dataclass
import os
from typing import Optional, Union
from src.app.core.handlers.error import DatabaseUnavailable
from src.infra.core.interfaces.database import IDatabase
from redis.asyncio import client

@dataclass
class RedisCreds:
    password: str

class Redis(IDatabase[client.Redis, RedisCreds]):

    def __init__(self,
                 host: str,
                 port: int = 6379) -> None:
        self.host = host
        self.port = port
        self.client: Union[client.Redis, None] = None

    async def connect(self, 
                      credentials: Optional[RedisCreds] = None) -> client.Redis:
        r_client = client.Redis(host=self.host, 
                                port=self.port)
        
        ping = await r_client.ping()

        if ping is False:
            raise DatabaseUnavailable("Was not possible to connect on Redis.")
        
        self.client = r_client
        print("[Redis] Connected Successfully!")
        return r_client
    
    async def disconnect(self) -> bool:
        if self.client is None: return True
        await self.client.close()
        print("[Redis] Disconnected Successfully!")
        return True
    
redis = Redis(host=os.getenv("REDIS_HOST", "localhost"),
              port=int(os.getenv("REDIS_PORT", 6379)))