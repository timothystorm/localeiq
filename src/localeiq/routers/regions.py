from fastapi import APIRouter, Path, HTTPException, status, Depends

from localeiq.models.region import Region
from localeiq.services.regions_service import RegionService

router = APIRouter(prefix="/regions")


def get_region_service() -> RegionService:
    return RegionService()


@router.get("/{country}/{postal}", response_model=Region)
def get_region_by_country(
    country: str = Path(
        ..., min_length=2, max_length=2, description="ISO 3166-1 alpha-2 country code"
    ),
    postal: str = Path(..., min_length=3, max_length=10),
    service: RegionService = Depends(get_region_service),
):
    """
    Get region details by country and postal code.
    """
    region = service.get_region_by_country_postal(country.lower(), postal)
    if region is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Region not found."
        )
    return region


@router.get("/{postal}", response_model=Region)
def get_region_by_postal_only(
    postal: str = Path(..., min_length=3, max_length=10),
    service: RegionService = Depends(get_region_service),
):
    """
    Get region details using only the postal code.
    Raises 409 Conflict if ambiguous and requires country specification.
    """
    print("hello")
    result = service.get_region_by_postal(postal)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Region not found."
        )
    if isinstance(result, list):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "message": "Postal code is ambiguous. Please specify a country.",
                "suggest": [
                    f"{router.prefix}/{r.location.country.code.lower()}/{postal}"
                    for r in result
                ],
            },
        )
    return result
