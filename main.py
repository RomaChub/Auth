from contextlib import asynccontextmanager

from fastapi import FastAPI

import uvicorn

from core.config import settings
from jwt_auth.demo_jwt_auth import router as jwt_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=jwt_router, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
