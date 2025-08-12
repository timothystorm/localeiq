from typing import List, Optional

from fastapi import APIRouter
from fastapi.params import Header

from localeiq.models.country import Country
from localeiq.services.service_factory import get_country_service

router = APIRouter()


@router.get("/countries", response_model=List[Country])
async def get_country_list(
    x_locale: Optional[str] = Header(default="en-US", alias="x-locale")
) -> List[Country]:
    """
    Returns a list of all countries with localized names based on the provided locale.
        If no locale is provided, defaults to 'en-US'.
    :param x_locale: The locale to filter country names by, defaults to 'en-US'.
        If x-locale is provided it must be a valid ISO 639-1 language code
            - ex. en-US, fr-CA.
    :return: A list of Country objects with localized names.
    """
    async with get_country_service() as service:
        return await service.get_country_list(language_code=x_locale)
