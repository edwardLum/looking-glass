from fastapi import APIRouter

from app.services.keywords import keyword_suggestion

router = APIRouter()

@router.get("/")
async def get_keywords(keyword_theme: str, number_of_keywords: int = 5):
    return keyword_suggestion(keyword_theme, number_of_keywords)
