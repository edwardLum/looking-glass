from fastapi import APIRouter

from app.services.keywords import KeywordSuggestion

router = APIRouter()

@router.get("/")
async def get_keywords(keyword_theme: str):
    suggestion = KeywordSuggestion(keyword_theme)
    return suggestion.get_keywords()
