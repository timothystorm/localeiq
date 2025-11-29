from typing import List

from fastapi import APIRouter

from date_time.service.time_service import TimeService

router = APIRouter(prefix="/v1")


@router.get(
    "/timezone",
    response_model=List[str],
    description="Returns a list of allowed timezones",
)
async def get_timezone_list() -> List[str]:
    return list(sorted(TimeService.list_timezones()))
