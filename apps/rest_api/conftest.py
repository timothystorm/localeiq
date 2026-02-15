"""
Shared test fixtures for rest_api module.

Provides common fixtures for API testing including:
- FastAPI test client
- Fake clock for time-based testing
- Mock services and repositories
"""

import pytest
from typing import Generator
import pendulum


try:
    from rest_api.service.chrono.clock import RealClock

    class FakeClock(RealClock):
        """
        A fake clock implementation for testing purposes that always returns a fixed time.

        Usage:
            @pytest.fixture
            def service(fake_clock):
                return TimeService(clock=fake_clock)
        """

        def __init__(self, fixed_time: pendulum.DateTime | None = None):
            self.fixed_time = fixed_time or pendulum.now("UTC")

        def now(self, tz: str) -> pendulum.DateTime:
            return self.fixed_time.in_timezone(tz)

        def set_time(self, dt: pendulum.DateTime):
            """Update the fixed time for the clock."""
            self.fixed_time = dt
except ImportError:
    # If imports fail, tests that need these will fail with clear errors
    pass


@pytest.fixture
def fake_clock():
    """
    Provides a FakeClock instance with a fixed time.
    Default time: 2025-11-15T10:23:00 UTC
    """
    return FakeClock(pendulum.datetime(2025, 11, 15, 10, 23, tz="UTC"))


@pytest.fixture
def test_client() -> Generator:
    """
    Provides a FastAPI TestClient for API integration tests.

    Usage:
        def test_endpoint(test_client):
            response = test_client.get("/v1/time/now")
            assert response.status_code == 200

    Note: Import is delayed to avoid loading full app during test collection.
    """
    from fastapi.testclient import TestClient
    from rest_api.start import create_app

    app = create_app()
    with TestClient(app) as client:
        yield client


@pytest.fixture
def utc_time() -> pendulum.DateTime:
    """Provides a fixed UTC datetime for consistent testing."""
    return pendulum.datetime(2025, 11, 15, 10, 23, tz="UTC")


@pytest.fixture
def sample_timezones() -> list[str]:
    """Provides a list of commonly tested timezones."""
    return [
        "UTC",
        "America/Denver",
        "America/New_York",
        "Europe/London",
        "Asia/Tokyo",
    ]
