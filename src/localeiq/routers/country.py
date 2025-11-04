from typing import List, Optional

from fastapi import APIRouter, Header

from localeiq.models.country import Country

router = APIRouter()


@router.get("/countries", response_model=List[Country])
async def get_countries(
        x_locale: Optional[str] = Header(default="en-US", alias="x-locale")
) -> List[Country]:
    """
    Returns a static list of countries.
    :return: A list of Country objects.
    """
    return [
        Country(code="US", name="United States"),
        Country(code="CA", name="Canada"),
        Country(code="GB", name="United Kingdom"),
        Country(code="FR", name="France"),
        Country(code="DE", name="Germany"),
    ]
