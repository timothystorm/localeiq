from pydantic import BaseModel

class TimeRequest(BaseModel):
    timezone: str


class TimeResponse(BaseModel):
    iso_8601: str
    dst: bool