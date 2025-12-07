import pendulum
from pendulum.tz.exceptions import InvalidTimezone

from date_time.service.clock import RealClock
from date_time.service.time_service import TimeService, to_valid_timezone


class FakeClock(RealClock):
    """
    A fake clock implementation for testing purposes that always returns a fixed time.
    """

    def __init__(self, fixed_time: pendulum.DateTime = pendulum.now()):
        self.fixed_time = fixed_time

    def now(self, tz: str) -> pendulum.DateTime:
        return self.fixed_time.in_timezone(tz)


class TestNow:
    def test_now(self):
        fixed = pendulum.datetime(2025, 11, 15, 10, 23, tz="UTC")
        service = TimeService(clock=FakeClock(fixed))

        response = service.now("America/Denver")
        assert response.in_timezone("America/Denver")
        assert response.to_iso8601_string() == "2025-11-15T03:23:00-07:00"
        assert response.is_dst() is False

    def test_now_invalid_timezone(self):
        fixed = pendulum.datetime(2025, 11, 15, 10, 23, tz="UTC")
        service = TimeService(clock=FakeClock(fixed))

        try:
            service.now("XXX/YYY")
        except InvalidTimezone as e:
            assert (
                str(e) == "Invalid timezone: XXX/YYY, try using `to_valid_timezone()`"
            )
        else:
            assert False, "Expected InvalidTimezone exception"

    def test_now_utc_leap_year(self):
        fixed = pendulum.datetime(2020, 2, 29, 12, 0, tz="UTC")  # Leap year date
        service = TimeService(clock=FakeClock(fixed))

        response = service.now("UTC")
        assert response.to_iso8601_string() == "2020-02-29T12:00:00Z"
        assert response.is_dst() is False

    def test_now_dst_transition(self):
        # Test a time during the DST transition in New York (March 8, 2020)
        fixed = pendulum.datetime(2020, 3, 8, 7, 30, tz="UTC")  # 2:30 AM UTC
        service = TimeService(clock=FakeClock(fixed))

        ny_response = service.now("America/New_York")
        assert (
            ny_response.to_iso8601_string() == "2020-03-08T03:30:00-04:00"
        )  # After DST starts
        assert ny_response.is_dst() is True

        den_response = service.now("America/Denver")
        assert (
            den_response.to_iso8601_string() == "2020-03-08T00:30:00-07:00"
        )  # Before DST starts
        assert den_response.is_dst() is False


class TestConvert:
    def test_convert(self):
        service = TimeService(clock=FakeClock())

        response = service.convert(
            "2025-11-15T10:23:00", from_tz="UTC", to_tz="America/Denver"
        )
        assert response.in_timezone("America/Denver")
        assert response.to_iso8601_string() == "2025-11-15T03:23:00-07:00"
        assert response.is_dst() is False

    def test_convert_different_timezones(self):
        service = TimeService(clock=FakeClock())

        response = service.convert(
            "2025-06-15T12:00:00", from_tz="Europe/Berlin", to_tz="America/New_York"
        )
        assert response.in_timezone("America/New_York")
        assert response.to_iso8601_string() == "2025-06-15T06:00:00-04:00"
        assert response.is_dst() is True

    def test_convert_invalid_timezone(self):
        service = TimeService(clock=FakeClock())

        try:
            service.convert(
                "2025-11-15T10:23:00", from_tz="XXX/YYY", to_tz="America/Denver"
            )
        except InvalidTimezone as e:
            assert str(e) == "Invalid timezone XXX/YYY"
        else:
            assert False, "Expected InvalidTimezone exception"


class TestTimezoneUtils:
    def test_list_timezones(self):
        from date_time.service.time_service import list_timezones

        timezones = list_timezones()
        assert "America/Denver" in timezones
        assert "UTC" in timezones
        assert "Europe/Berlin" in timezones
        assert (
            len(timezones) >= 598
        )  # As of Dec. 2025, there are 598 IANA timezones and variations available

    def test_to_valid_timezone_valid(self):
        # valid timezones
        assert to_valid_timezone("America/Denver") == "America/Denver"
        assert to_valid_timezone("UTC") == "UTC"

    def test_to_valid_timezone_missing(self):
        # missing timezones
        assert to_valid_timezone(None) == "UTC"
        assert to_valid_timezone("") == "UTC"

    def test_to_valid_timezone_suggestion(self):
        # invalid timezones with possible suggestion
        try:
            to_valid_timezone("America/Denvur")
        except InvalidTimezone as e:
            assert str(e) == "Invalid timezone, did you mean 'America/Denver'"
        else:
            assert False, "Expected InvalidTimezone exception"

    def test_to_valid_timezone_no_suggestion(self):
        # invalid timezones without suggestion
        try:
            to_valid_timezone("XXX/YYY")
        except InvalidTimezone as e:
            assert str(e) == "Invalid timezone XXX/YYY"
        else:
            assert False, "Expected InvalidTimezone exception"
