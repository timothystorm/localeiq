from localeiq.models.coordinates import Coordinates
from localeiq.models.country import Country
from localeiq.models.location import Location
from localeiq.models.region import Region
from localeiq.models.time_zone import TimeZone


class RegionRepository:
    def __init__(self):
        # in-memory for now
        self._data = [
            Region(
                coordinates=Coordinates(latitude=39.0902, longitude=-104.8572),
                location=Location(
                    city="Monument",
                    country=Country(code="US", name="United States"),
                    postal_code="80132",
                ),
                time_zone=TimeZone(
                    utc_offset="-07:00",
                    iana="America/Denver",
                    std_abbr="MST",
                    dst_abbr="MDT",
                ),
            ),
            Region(
                coordinates=Coordinates(latitude=34.0901, longitude=-118.4065),
                location=Location(
                    city="Beverly Hills",
                    country=Country(code="US", name="United States"),
                    postal_code="90210",
                ),
                time_zone=TimeZone(
                    utc_offset="-08:00",
                    iana="America/Los_Angeles",
                    std_abbr="PST",
                    dst_abbr="PDT",
                ),
            ),
            Region(
                coordinates=Coordinates(latitude=40.7506, longitude=-73.9970),
                location=Location(
                    city="New York",
                    country=Country(code="US", name="United States"),
                    postal_code="10001",
                ),
                time_zone=TimeZone(
                    utc_offset="-05:00",
                    iana="America/New_York",
                    std_abbr="EST",
                    dst_abbr="EDT",
                ),
            ),
            Region(
                coordinates=Coordinates(latitude=33.7490, longitude=-84.3880),
                location=Location(
                    city="Atlanta",
                    country=Country(code="US", name="United States"),
                    postal_code="30301",
                ),
                time_zone=TimeZone(
                    utc_offset="-05:00",
                    iana="America/New_York",
                    std_abbr="EST",
                    dst_abbr="EDT",
                ),
            ),
            Region(
                coordinates=Coordinates(latitude=42.6526, longitude=-73.7562),
                location=Location(
                    city="Albany Metro",
                    country=Country(code="US", name="United States"),
                    postal_code="12345",
                ),
                time_zone=TimeZone(
                    utc_offset="-05:00",
                    iana="America/New_York",
                    std_abbr="EST",
                    dst_abbr="EDT",
                ),
            ),
            Region(
                coordinates=Coordinates(latitude=43.6532, longitude=-79.3832),
                location=Location(
                    city="Windsor Subzone",
                    country=Country(code="CA", name="Canada"),
                    postal_code="12345",
                ),
                time_zone=TimeZone(
                    utc_offset="-05:00",
                    iana="America/Toronto",
                    std_abbr="EST",
                    dst_abbr="EDT",
                ),
            ),
        ]  # For now, in-memory

    def find_by_postal(self, postal: str):
        print(postal)
        return [r for r in self._data if r.location.postal_code == postal]

    def find_by_country_and_postal(self, country: str, postal: str):
        return [
            r
            for r in self._data
            if r.location.postal_code == postal
            and r.location.country.code.lower() == country.lower()
        ]
