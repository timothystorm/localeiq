import difflib
from typing import List
from zoneinfo import available_timezones

import pendulum
from pendulum.tz.exceptions import InvalidTimezone
from pydantic import BaseModel


class TimeResponse(BaseModel):
    """
    Response model for current time information.
    """
    iso_8601: str
    dst: bool
    timestamp: float


class TimeService:
    """

    """
    @staticmethod
    def now(tz_name: str) -> TimeResponse:
        """
        :return: current time information for the given timezone.
        """
        now = pendulum.now(tz=tz_name)
        return TimeResponse(
            dst=now.is_dst(),
            iso_8601=now.to_iso8601_string(),
            timestamp=now.timestamp() * 1000,  # milliseconds
        )

    @staticmethod
    def list_timezones() -> List[str]:
        return list(available_timezones())

    @staticmethod
    def validate_timezone(tz: str | None) -> str | None:
        """
        Validates the given timezone string against available IANA timezones.
        If the timezone is invalid an IInvalidTimezone exception is raised with a suggestion if possible.

        :param tz: Timezone string to validate
        :return: Valid timezone string or raises ValueError
        """
        if tz == "" or tz is None or tz in available_timezones():
            return tz

        matches = difflib.get_close_matches(tz, available_timezones(), n=1, cutoff=0.6)
        raise InvalidTimezone(
            f"Invalid timezone, did you mean '{matches[0]}'" if matches else f"Invalid timezone")
