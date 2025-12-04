import difflib
from typing import List
from zoneinfo import available_timezones

import pendulum
from pendulum.tz.exceptions import InvalidTimezone

from date_time.service.clock import Clock, RealClock


def list_timezones() -> List[str]:
    """
    Lists all available IANA timezones.
    """
    return list(available_timezones())


def to_valid_timezone(tz: str | None) -> str:
    """
    Converts the given timezone string into a valid  IANA timezones.
    If the timezone is invalid an InvalidTimezone exception is raised with a suggestion if possible.

    examples of valid timezones: "America/Denver", "UTC", "Europe/Berlin".

    :param tz: Timezone string to convert
    :return: Valid timezone string or raises ValueError
    :raises InvalidTimezone: If the timezone is invalid
    """
    if tz == "" or tz is None:
        return "UTC"
    elif tz in available_timezones():
        return tz

    # Suggest the closest matching timezone
    matches = difflib.get_close_matches(tz, available_timezones(), n=1, cutoff=0.6)
    raise InvalidTimezone(
        f"Invalid timezone, did you mean '{matches[0]}'"
        if matches
        else f"Invalid timezone {tz}"
    )


class TimeService:
    """
    Service for handling time-related operations.
    """

    def __init__(self, clock: Clock = RealClock()):
        """
        :param clock: Clock implementation to use for getting the current time. Defaults to RealClock.
        """
        self._clock = clock

    def now(self, tz: str) -> pendulum.DateTime:
        """
        :return: current time information for the given timezone.
        """
        try:
            return self._clock.now(tz)
        except InvalidTimezone as e:
            raise InvalidTimezone(
                f"Invalid timezone: {tz}, try using `to_valid_timezone()`"
            ) from e

    def convert(self, dt: str, from_tz: str, to_tz: str = "UTC") -> pendulum.DateTime:
        """
        Converts the given datetime string from one timezone to another.

        :param dt: Datetime string to convert.
        :param from_tz: Source timezone.
        :param to_tz: Target timezone. Defaults to "UTC".
        :return: Converted datetime in the target timezone.
        """
        source_tz = to_valid_timezone(from_tz)
        target_tz = to_valid_timezone(to_tz)
        parsed_dt = self._clock.parse(dt, tz=source_tz)
        return parsed_dt.in_timezone(target_tz)
