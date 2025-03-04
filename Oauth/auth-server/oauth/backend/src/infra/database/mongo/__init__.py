from dataclasses import dataclass
import os
from typing import Optional
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.app.core.handlers.error import InvalidCredentials
from src.infra.core.interfaces.database import IDatabase
from src.infra.database.mongo.models.config import Config
from src.infra.database.mongo.models.token import Tokens

@dataclass
class MongoCreds:
    username: str
    password: str

class MongoDB(IDatabase[AsyncIOMotorClient, MongoCreds]):
    def __init__(self,
                 host: Optional[str] = "mongo",
                 driver: str = "mongodb"): 
        self.host = host
        self.driver = driver
        self.client: Optional[AsyncIOMotorClient] = None
        
    async def connect(self, 
                      credentials: Optional[MongoCreds] = None) -> AsyncIOMotorClient:
        if credentials is None:
            raise InvalidCredentials("Could not connect on mongo due lack of credentials.")
        self.client = AsyncIOMotorClient(f"{self.driver}://{credentials.username}:{credentials.password}@{self.host}",
                                         server_api=ServerApi("1"))
        await self.add_models()
        print("[Mongo] Connected Successfully!")
        return self.client
    
    async def add_models(self):
        if self.client is None:
            return
        await init_beanie(database=self.client.get_database("auth"), document_models=[
            Config,
            Tokens
        ])

    async def disconnect(self) -> bool:
        if self.client is None: return False
        self.client.close()
        print("[Mongo] Disconnected Successfully!")
        return True


database = MongoDB(host=os.getenv("MONGO_HOST", "localhost"),
                   driver=os.getenv("MONGO_DRIVER", "mongodb"))