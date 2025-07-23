from localeiq.models.coordinates import Coordinates
from localeiq.models.country import Country
from localeiq.models.location import Location
from localeiq.models.region import Region
from localeiq.models.time_zone import TimeZone


def get_region_by_postal(postal: str) -> Region | None:
    match postal:
        case "80132":
            return Region(
                coordinates=Coordinates(latitude=39.0902, longitude=-104.8572),
                location=Location(
                    city="Monument",
                    country=Country(code="US", name="United States"),
                ),
                time_zone=TimeZone(
                    utc_offset="-07:00",
                    iana="America/Denver",
                    std_abbr="MST",
                    dst_abbr="MDT",
                ),
            )
        case "90210":
            return Region(
                coordinates=Coordinates(latitude=34.0901, longitude=-118.4065),
                location=Location(
                    city="Beverly Hills",
                    country=Country(code="US", name="United States"),
                ),
                time_zone=TimeZone(
                    utc_offset="-08:00",
                    iana="America/Los_Angeles",
                    std_abbr="PST",
                    dst_abbr="PDT",
                ),
            )
        case "10001":
            return Region(
                coordinates=Coordinates(latitude=40.7506, longitude=-73.9970),
                location=Location(
                    city="New York",
                    country=Country(code="US", name="United States"),
                ),
                time_zone=TimeZone(
                    utc_offset="-05:00",
                    iana="America/New_York",
                    std_abbr="EST",
                    dst_abbr="EDT",
                ),
            )
        case "30301":
            return Region(
                coordinates=Coordinates(latitude=33.7490, longitude=-84.3880),
                location=Location(
                    city="Atlanta",
                    country=Country(code="US", name="United States"),
                ),
                time_zone=TimeZone(
                    utc_offset="-05:00",
                    iana="America/New_York",
                    std_abbr="EST",
                    dst_abbr="EDT",
                ),
            )
        case _:
            return None
