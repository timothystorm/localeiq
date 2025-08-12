import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

from localeiq.routers.countries_router import router
from localeiq.models.country import Country


@pytest.fixture
def app():
    app = FastAPI()
    app.include_router(router)
    return app


@pytest.fixture
def mock_country_service():
    mock_service = AsyncMock()
    mock_service.__aenter__.return_value = mock_service
    mock_service.get_country_list.return_value = [
        Country(code="US", name="United States"),
        Country(code="ES", name="Spain"),
        Country(code="FR", name="France"),
    ]
    return mock_service


@pytest.mark.parametrize(
    "locale,expected_locale",
    [
        (None, "en-US"),
        ("es_US", "es_US"),
        ("es-us", "es-us"),
        ("ES-US", "ES-US"),
        ("xx_YY", "xx_YY"),
    ],
)
def test_get_country_list_locales(app, mock_country_service, locale, expected_locale):
    with patch(
        "localeiq.routers.countries_router.get_country_service",
        return_value=mock_country_service,
    ):
        client = TestClient(app)
        headers = {}
        if locale is not None:
            headers["x-locale"] = locale

        response = client.get("/countries", headers=headers)

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 3
        assert all("code" in country and "name" in country for country in data)
        mock_country_service.get_country_list.assert_awaited_with(
            language_code=expected_locale
        )


def test_get_countries_count(app, mock_country_service):
    with patch(
        "localeiq.routers.countries_router.get_country_service",
        return_value=mock_country_service,
    ):
        client = TestClient(app)

        response = client.get("/countries/count")

        assert response.status_code == 200
        data = response.json()
        assert data == {"count": 3}
        mock_country_service.get_country_list.assert_awaited_with()
