from fastapi import FastAPI
from app.api.endpoints.keywords import router as keyword_router

app = FastAPI()

app.include_router(keyword_router, prefix="/keywords", tags=["keywords"])
