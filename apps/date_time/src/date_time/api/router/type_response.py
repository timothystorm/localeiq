from pydantic import BaseModel


class TimeResponse(BaseModel):
    """
    Response model for current time information.
    """

    # current time in ISO 8601 format
    iso_8601: str

    # whether daylight saving time is in effect
    dst: bool

    # current time in milliseconds since epoch
    timestamp: float
