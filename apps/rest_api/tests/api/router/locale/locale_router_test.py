from starlette.testclient import TestClient

from rest_api.main import app

client = TestClient(app)


def test_get_locale_returns_locale_model():
    response = client.get("/v1/locale/en-US")
    assert response.status_code == 200

    payload = response.json()
    assert "locale" in payload
    assert isinstance(payload["locale"], str)

    from rest_api.api.router.locale.locale_dto import Locale

    Locale.model_validate(payload)  # will raise if not a valid Locale
