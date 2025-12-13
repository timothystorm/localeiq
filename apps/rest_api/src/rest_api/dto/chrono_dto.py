from typing import Optional

from pydantic import BaseModel, Field


class DateTime(BaseModel):
    """
    Response model for current time information.
    """

    iso_8601: str = Field(
        ...,
        description="Current time in ISO 8601 format",
        examples=["2020-01-20T00:00:00", "2030-03-08T00:30:00-07:00"],
    )

    dst: bool = Field(
        ...,
        description="Whether daylight saving time is in effect",
        examples=[True, False],
    )

    ts: float = Field(
        ...,
        description="Current time in milliseconds since epoch",
        examples=[1579478400000],
    )


class DateTimeResponse(DateTime):
    tz: str = Field(
        "UTC",
        description="Timezone of the current time",
        examples=["UTC", "America/Denver"],
    )


class DateTimeConvertInput(BaseModel):
    """
    Response model for converted time information.
    """

    dt: str = Field(
        ...,
        description="DateTime string to convert",
        examples=["2025-11-15T10:23:00", "2025-06-15T12:00:00"],
    )

    from_tz: Optional[str] = Field(
        "UTC",
        description="Timezone of the current time",
        examples=["UTC", "America/Denver"],
    )

    to_tz: Optional[str] = Field(
        "UTC",
        description="Timezone to convert the time to",
        examples=["America/Denver", "Europe/Berlin"],
    )


class DateTimeConvertResponse(DateTime):
    original_request: Optional[DateTimeConvertInput] = Field(
        None, description="The original conversion request details"
    )
