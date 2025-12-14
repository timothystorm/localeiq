from fastapi.testclient import TestClient

from rest_api.main import app

client = TestClient(app)


def test_get_current_time():
    assert True


def test_get_current_time_default_timezone():
    assert True
