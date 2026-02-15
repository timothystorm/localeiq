"""
Shared test fixtures for data_store module.

Provides common fixtures for database testing including:
- Test database setup/teardown
- Repository fixtures
- Mock database connections
"""

import pytest
from unittest.mock import Mock, MagicMock


@pytest.fixture(scope="session")
def test_db_url() -> str:
    """
    Provides a test database URL.
    Override with environment variable TEST_DB_URL if needed.
    """
    import os

    return os.getenv(
        "TEST_DB_URL",
        "postgresql+psycopg2://test_user:test_pass@localhost:5432/localeiq_test",
    )


@pytest.fixture
def mock_db_session():
    """
    Provides a mock database session for unit tests that don't need a real DB.

    Usage:
        def test_repository(mock_db_session):
            repo = LocaleRepoImpl(session=mock_db_session)
            # Test repository logic without database
    """
    session = MagicMock()
    session.query = Mock()
    session.add = Mock()
    session.commit = Mock()
    session.rollback = Mock()
    session.close = Mock()
    return session


@pytest.fixture
def sample_locale_data() -> dict:
    """Provides sample locale data for testing."""
    return {
        "locale_code": "en_US",
        "language": "English",
        "country": "United States",
        "language_code": "en",
        "country_code": "US",
    }
