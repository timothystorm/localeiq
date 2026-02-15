"""
Root-level pytest configuration and shared fixtures.

This conftest.py is automatically discovered by pytest and provides
fixtures available to all test modules across the entire workspace.
"""

import pytest


@pytest.fixture(scope="session")
def test_data_dir():
    """
    Returns the path to the test data directory.
    Override in submodule conftest.py if needed.
    """
    from pathlib import Path

    return Path(__file__).parent / "test_data"
