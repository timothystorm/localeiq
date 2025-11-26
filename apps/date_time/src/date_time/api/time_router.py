from fastapi import APIRouter, HTTPException
from pendulum.tz.exceptions import InvalidTimezone

from date_time.model.date_time_dto import TimeResponse, TimeRequest
from date_time.service.time_service import get_current_time
from utils.configuration import get_config

router = APIRouter(prefix='/v1')


@router.post("/time", response_model=TimeResponse)
async def time(request: TimeRequest) -> TimeResponse:
    try:
        result = get_current_time(request.timezone)
        return TimeResponse(**result)
    except InvalidTimezone:
        raise HTTPException(status_code=400, detail=str(f'Invalid timezone: {request.timezone}'))
