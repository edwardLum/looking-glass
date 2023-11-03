from fastapi import APIRouter

from app.services.campaign_structure import campaign_structure_suggestion

router = APIRouter()

@router.get("/")
async def get_campaign_structure(business_category: str):
    """
    Retrieve AI-powered campaign structure suggestions for the given business category.

    Args:
    - business_category (str): The category of the business for which campaign structure suggestions are required.

    Returns:
    JSON: AI-powered suggestions for campaign structure.

    Example:
    >>> get_campaign_structure("women's shoes")
    {
        {"campaigns":[{"campaign_name":"Casual Shoes",
                       "ad_groups":[{"ad_group_name":"Sneakers"},
                                    {"ad_group_name":"Flats"}
        ...
    }
    """
    return campaign_structure_suggestion(business_category)
