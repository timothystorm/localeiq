from fastapi.testclient import TestClient

from localeiq.main import app

client = TestClient(app)


def test_context_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to LocaleIQ"}
