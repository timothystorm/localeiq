from abc import ABC, abstractmethod
from typing import cast

import pendulum
from pendulum import DateTime


class Clock(ABC):
    """
    Abstract clock interface for getting the current time.
    """

    @abstractmethod
    def now(self, tz_name: str) -> DateTime:
        pass

    @abstractmethod
    def parse(self, dt_str: str, tz: str) -> DateTime:
        pass


class RealClock(Clock):
    """
    Real clock implementation using pendulum to get the current time.
    """

    def now(self, tz_name: str) -> DateTime:
        return pendulum.now(tz=tz_name)

    def parse(self, dt_str: str, tz: str) -> DateTime:
        # pendulum.parse returns Date | DateTime | Time | Duration | None, but with valid inputs it will always return DateTime
        return cast(DateTime, pendulum.parse(dt_str, tz=tz))
