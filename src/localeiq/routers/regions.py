from fastapi import APIRouter, HTTPException, Path
from starlette import status

from localeiq.models.region import Region
from localeiq.services.region_service import get_region_by_postal

router = APIRouter()


@router.get(
    "/regions/{postal}",
    response_model=Region,
    tags=["Region"],
    summary="Get region info",
    description="Returns geographic and timezone info for a given postal code.",
    responses={
        404: {"description": "Region not found"},
        422: {"description": "Validation error"},
    },
)
def get_region(
    postal: str = Path(
        ...,
        min_length=3,
        max_length=10,
        description="Postal code to look up. Must be between 3–10 characters.",
        example="80132",
    )
):
    """
    Look up region metadata based on a postal code.

    Args:
        postal (str): The postal code to look up.

    Returns:
        Region: Structured region data including coordinates, location, and time zone.
    """
    region = get_region_by_postal(postal)
    if region is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Region not found for postal code: {postal}",
        )
    return region
