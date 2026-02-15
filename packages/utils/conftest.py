"""
Shared test fixtures for utils module.

Provides common fixtures for testing utility functions.
"""

import pytest
from pathlib import Path
from typing import Generator
import tempfile
import os


@pytest.fixture
def temp_env_file() -> Generator[Path, None, None]:
    """
    Creates a temporary .env file for testing configuration loading.

    Usage:
        def test_config(temp_env_file):
            temp_env_file.write_text("KEY=value")
            config = load_config(temp_env_file)
            assert config.KEY == "value"
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
        temp_path = Path(f.name)

    yield temp_path

    # Cleanup
    if temp_path.exists():
        temp_path.unlink()


@pytest.fixture
def clean_env() -> Generator[None, None, None]:
    """
    Saves current environment variables and restores them after test.
    Useful for testing environment-dependent code.

    Usage:
        def test_env_loading(clean_env):
            os.environ["TEST_VAR"] = "test_value"
            # Test code that reads TEST_VAR
            # Environment is automatically restored after test
    """
    original_env = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def sample_config_data() -> dict:
    """Provides sample configuration data for testing."""
    return {
        "DEBUG": True,
        "LOG_LEVEL": "INFO",
        "API_KEY": "test_key_12345",
        "MAX_CONNECTIONS": 10,
    }
