from fastapi import FastAPI
from app.api.endpoints.keywords import router as keyword_router
from app.api.endpoints.campaign_structure import router as campaign_structure_router

app = FastAPI()

app.include_router(keyword_router, prefix="/keywords", tags=["keywords"])

app.include_router(campaign_structure_router, prefix="/campaign_structure", tags=["campaign_structure"])
