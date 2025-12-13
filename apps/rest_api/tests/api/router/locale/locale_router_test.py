from starlette.testclient import TestClient

from data_store.dto.locale_dto import LocaleDto
from rest_api.main import app

client = TestClient(app)


def test_get_locale_returns_locale_model():
    response = client.get("/v1/locale/en-US")
    assert response.status_code == 200

    payload = response.json()

    LocaleDto.model_validate(payload)  # will raise if not a valid Locale
