from typing import List, Optional

from fastapi import APIRouter
from fastapi.params import Depends, Header

from localeiq.models.country import Country, CountryCountResponse
from localeiq.services.country_service import CountryService

router = APIRouter()


def get_country_service() -> CountryService:
    return CountryService()


@router.get("/countries", response_model=List[Country])
def get_country_list(
    x_locale: Optional[str] = Header(default="en-US", alias="x-locale"),
    service: CountryService = Depends(get_country_service),
) -> List[Country]:
    """
    Returns a list of all countries with localized names based on the provided locale.
        If no locale is provided, defaults to 'en-US'.
    :param x_locale: The locale to filter country names by, defaults to 'en-US'.
        If x-locale is provided it must be a valid ISO 639-1 language code
            - ex. en-US, fr-CA.
    :param service: The CountryService instance to fetch country data.
    :return: A list of Country objects with localized names.
    """
    return service.get_country_list(locale=x_locale)


@router.get("/countries/count")
def get_countries_count(
    service: CountryService = Depends(get_country_service),
) -> CountryCountResponse:
    """
    Returns the total number of countries available.
    This endpoint does not require any parameters.
    :param service: The CountryService instance to fetch country data.
    :return: A CountryCountResponse containing the count of countries.
    """
    return CountryCountResponse(count=len(service.get_country_list()))
