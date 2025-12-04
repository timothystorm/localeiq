from typing import Optional

from pydantic import BaseModel


class DateTimeDto(BaseModel):
    """
    Response model for current time information.
    """

    # current time in ISO 8601 format
    iso_8601: str

    # whether daylight saving time is in effect
    dst: bool

    # current time in milliseconds since epoch
    ts: float


class DateTimeResponse(DateTimeDto):
    pass


class DateTimeConvertDto(BaseModel):
    """
    Response model for converted time information.
    """

    from_tz: Optional[str] = None
    to_tz: Optional[str] = None


class DateTimeConvertInput(DateTimeConvertDto):
    dt: str


class DateTimeConvertResponse(DateTimeDto):
    original_request: Optional[DateTimeConvertInput] = None
