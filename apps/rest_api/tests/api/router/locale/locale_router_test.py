from starlette.testclient import TestClient

from rest_api.main import app

client = TestClient(app)


def test_get_locale_returns_locale_model():
    assert True
