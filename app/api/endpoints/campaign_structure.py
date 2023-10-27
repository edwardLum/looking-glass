from fastapi import APIRouter

from app.services.campaign_structure import campaign_structure_suggestion

router = APIRouter()

@router.get("/")
async def get_campaign_structure(business_category: str):
    return campaign_structure_suggestion(business_category)
