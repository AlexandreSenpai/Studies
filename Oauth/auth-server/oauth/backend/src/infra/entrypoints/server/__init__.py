from contextlib import asynccontextmanager
import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.app.core.handlers.error import Error

from src.infra.database.redis import redis
from src.infra.database.mongo import MongoCreds, database
from src.infra.entrypoints.routes import router

@asynccontextmanager
async def lifespan(server: FastAPI):
    try:
        await database.connect(credentials=MongoCreds(username=os.getenv("DATABASE_USERNAME", ""),
                                                      password=os.getenv("DATABASE_PASSWORD", "")))
        await redis.connect()
        yield
    finally:
        await database.disconnect()
        await redis.disconnect()

server = FastAPI(lifespan=lifespan)

server.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://shogun.minorin.io",
        "https://auth.shogun.minorin.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

server.include_router(router)

@server.exception_handler(Error)
async def app_exception_handler(request: Request, exc: Error):
    return JSONResponse(
        status_code=exc.status,
        content={"message": exc.message,
                 "code": exc.code},
    )

@server.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc),
                 "code": 'INTERNAL_SERVER_ERROR'},
    )
