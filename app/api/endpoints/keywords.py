from fastapi import APIRouter

from app.services.keywords import keyword_suggestion

router = APIRouter()

@router.get("/")
async def get_keywords(keyword_theme: str, number_of_keywords: int = 5):
     """
    Retrieve AI-powered keyword suggestions based on a specific theme.

    Args:
    - keyword_theme (str): The main theme or topic for which keyword suggestions are desired.
    - number_of_keywords (int, optional): The number of keyword suggestions to retrieve. Defaults to 5.

    Returns:
    JSON: A list of OpenAI-powered keyword suggestions.

    Example:
    >>> get_keywords("boots", 3)
    {"keywords":["best boots","buy boots online","affordable boots"]}
    """
    return keyword_suggestion(keyword_theme, number_of_keywords)
