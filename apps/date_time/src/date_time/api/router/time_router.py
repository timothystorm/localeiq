from fastapi import APIRouter, HTTPException, Request
from pendulum.tz.exceptions import InvalidTimezone

from date_time.service.time_service import TimeService, TimeResponse

router = APIRouter(prefix="/v1")


@router.get("/time",
            response_model=TimeResponse,
            response_model_exclude_none=True,
            description="Returns the current time in the selected timezone or UTC if no timezone provided")
async def get_current_time(tz: str | None = None):
    try:
        good_tz = TimeService.validate_timezone(tz)
        return TimeService.now(good_tz or "UTC")
    except InvalidTimezone as e:
        raise HTTPException(
            status_code=400, detail=str(e)
        )
