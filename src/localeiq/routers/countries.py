from typing import List

from fastapi import APIRouter
from fastapi.params import Depends

from localeiq.models.country import Country, CountryCountResponse
from localeiq.services.country_service import CountryService

router = APIRouter()


def get_country_service() -> CountryService:
    return CountryService()


@router.get("/countries", response_model=List[Country])
def get_country_list(
    service: CountryService = Depends(get_country_service),
) -> List[Country]:
    return service.get_country_list()


@router.get("/countries/count")
def get_countries_count(
    service: CountryService = Depends(get_country_service),
) -> CountryCountResponse:
    """
    Returns the total number of countries available.
    """
    return CountryCountResponse(count=len(service.get_country_list()))
