from fastapi import APIRouter, Query, HTTPException

from localeiq.models.region import Region
from localeiq.services.region_service import get_region_by_postal

router = APIRouter(prefix="/api/v1/regions", tags=["Region"])


@router.get("", response_model=Region)
def get_regions_lookup(postal: str = Query(..., min_length=3, max_length=10)):
    """
    Return region information based on a postal code.
    """
    region = get_region_by_postal(postal)
    if region is None:
        raise HTTPException(status_code=404, detail="Region not found for postal code.")
    return region
