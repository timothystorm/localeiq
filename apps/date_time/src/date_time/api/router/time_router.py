from typing import List

from fastapi import APIRouter, HTTPException
from pendulum.tz.exceptions import InvalidTimezone

from date_time.api.router.type_response import TimeResponse
from date_time.service.time_service import (
    TimeService,
    to_valid_timezone,
    list_timezones,
)

router = APIRouter(prefix="/v1")


@router.get(
    "/time",
    response_model=TimeResponse,
    response_model_exclude_none=True,
    description="Returns the current time in the selected timezone or UTC if no timezone provided",
)
async def get_current_time(tz: str | None = None):
    """
    :param tz: IANA timezone string, e.g. "America/Denver". If not provided, UTC is used.
    :return: Current time information for the specified timezone.
    """
    try:
        valid_timezone = to_valid_timezone(tz)
        now = TimeService().now(tz=valid_timezone or "UTC")
        return TimeResponse(
            dst=now.is_dst(),
            iso_8601=now.to_iso8601_string(),
            timestamp=now.timestamp() * 1000,  # milliseconds
        )
    except InvalidTimezone as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/timezone",
    response_model=List[str],
    description="Returns a list of allowed timezones",
)
async def get_timezone_list() -> List[str]:
    """
    :return: A list of all available IANA timezones sorted alphabetically.
    """
    return list(sorted(list_timezones()))
