from typing import List

from fastapi import APIRouter, HTTPException
from pendulum.parsing import ParserError
from pendulum.tz.exceptions import InvalidTimezone

from date_time.api.router.date_time_dto import (
    DateTimeDto,
    DateTimeConvertResponse,
    DateTimeConvertInput,
)
from date_time.service.time_service import (
    TimeService,
    to_valid_timezone,
    list_timezones,
)

router = APIRouter(prefix="/v1/time", tags=["time"])


@router.get(
    "/zones",
    response_model=List[str],
    description="Returns a list of allowed timezones",
)
async def get_timezone_list() -> List[str]:
    """
    :return: A list of all available IANA timezones sorted alphabetically.
    """
    return list(sorted(list_timezones()))


@router.get(
    "/now",
    response_model=DateTimeDto,
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
        return DateTimeDto(
            dst=now.is_dst(),
            iso_8601=now.to_iso8601_string(),
            ts=now.timestamp() * 1000,  # milliseconds
        )
    except InvalidTimezone as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/convert",
    response_model=DateTimeConvertResponse,
    response_model_exclude_none=True,
    description="Converts time from one timezone to another",
)
async def post_convert(request: DateTimeConvertInput) -> DateTimeConvertResponse:
    try:
        valid_from_tz = to_valid_timezone(request.from_tz)
        valid_to_tz = to_valid_timezone(request.to_tz)
        convert = TimeService().convert(request.dt, valid_from_tz, valid_to_tz)
        return DateTimeConvertResponse(
            original_request=DateTimeConvertInput(
                dt=request.dt,
                from_tz=valid_from_tz,
                to_tz=valid_to_tz,
            ),
            dst=convert.is_dst(),
            iso_8601=convert.to_iso8601_string(),
            ts=convert.timestamp() * 1000,  # milliseconds
        )
    except (InvalidTimezone, ParserError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
