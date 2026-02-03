from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging, logger
from app.db import init_db
from contextlib import asynccontextmanager
from app.api.v1.auth import router as auth_router

setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting AetherDock", env=settings.APP_ENV)
    init_db()
    yield
    logger.info("Shutting down AetherDock", env=settings.APP_ENV)

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.include_router(auth_router, prefix="/api/v1")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)