from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints.keywords import router as keyword_router
from app.api.endpoints.campaign_structure import router as campaign_structure_router

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(keyword_router, prefix="/keywords", tags=["keywords"])

app.include_router(campaign_structure_router, prefix="/campaign_structure", tags=["campaign_structure"])
