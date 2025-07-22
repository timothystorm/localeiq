from localeiq.models.coordinates import Coordinates
from localeiq.models.country import Country
from localeiq.models.location import Location
from localeiq.models.region import Region
from localeiq.models.time_zone import TimeZone


def get_region_by_postal(postal: str) -> Region | None:
    if postal == "80132":
        return Region(
            coordinates=Coordinates(latitude=39.0902, longitude=-104.8572),
            location=Location(
                city="Monument",
                country=Country(code="US", name="United States"),
            ),
            time_zone=TimeZone(
                utc_offset="-07:00",
                iana="America/Denver",
                std_abbreviation="MST",
                dst_abbreviation="MDT",
            ),
        )
    return None
