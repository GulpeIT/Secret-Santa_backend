import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.models import db_helper
from src.config import settings
from src.api.v1 import router as main_router 

@asynccontextmanager
async def lifespan(app: FastAPI) :
    # on start app
    yield
    # on close app
    await db_helper.dispose()

app = FastAPI(
    debug=True,
    lifespan=lifespan,
)

origins = [ "http://localhost:8000", "http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=main_router
)

if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host=settings.app_run.host,
        port=settings.app_run.port,
        reload=True,
        reload_delay=3
    )
