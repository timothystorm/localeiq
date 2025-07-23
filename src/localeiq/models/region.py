from pydantic import BaseModel

from localeiq.models.coordinates import Coordinates
from localeiq.models.location import Location
from localeiq.models.time_zone import TimeZone


class Region(BaseModel):
    """
    Represents a geographic region, including coordinates, location, and time
    zone details.

    Attributes:
        coordinates (Coordinates): The latitude and longitude of the region.
        location (Location): The city and country associated with the region.
        time_zone (TimeZone): The time zone information, including offsets and
            abbreviations.
    """

    coordinates: Coordinates
    location: Location
    time_zone: TimeZone
