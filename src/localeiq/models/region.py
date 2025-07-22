from pydantic import BaseModel

from localeiq.models.coordinates import Coordinates
from localeiq.models.location import Location
from localeiq.models.time_zone import TimeZone


class Region(BaseModel):
    coordinates: Coordinates
    location: Location
    time_zone: TimeZone
