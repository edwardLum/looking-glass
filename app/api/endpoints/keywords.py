from fastAPI import APIRouter

router = APIRouter()

@router.get("/keywords/")
async def get_keywords(keyword_theme: str = "None"):
    pass
