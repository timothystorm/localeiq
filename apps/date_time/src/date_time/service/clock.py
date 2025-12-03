from abc import ABC, abstractmethod

import pendulum
from pendulum import DateTime


class Clock(ABC):
    """
    Abstract clock interface for getting the current time.
    """

    @abstractmethod
    def now(self, tz_name: str) -> DateTime:
        pass


class RealClock(Clock):
    """
    Real clock implementation using pendulum to get the current time.
    """

    def now(self, tz_name: str) -> DateTime:
        return pendulum.now(tz=tz_name)
