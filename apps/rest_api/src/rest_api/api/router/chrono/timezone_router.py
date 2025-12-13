from typing import List

from fastapi import APIRouter

from rest_api.service.chrono.chrono_service import list_timezones

router = APIRouter(prefix="/v1/timezone", tags=["timezone"])


@router.get(
    "/",
    response_model=List[str],
    description="Returns a list of allowed timezones",
)
async def get_timezone_list() -> List[str]:
    """
    :return: A list of all available IANA timezones sorted alphabetically.
    """
    return list(sorted(list_timezones()))
