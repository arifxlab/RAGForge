from fastapi import FastAPI

from app.api.v1 import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Production-ready AI Knowledge Platform powered by Retrieval-Augmented Generation (RAG).",
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "project": settings.APP_NAME,
        "status": "running",
        "version": settings.APP_VERSION,
    }


app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX,
)