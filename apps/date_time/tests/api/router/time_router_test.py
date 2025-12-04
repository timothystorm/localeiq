from fastapi.testclient import TestClient

from date_time.main import app

client = TestClient(app)


def test_get_current_time():
    response = client.get("/v1/time/now", params={"timezone": "America/Denver"})
    assert response.status_code == 200
    data = response.json()

    assert "iso_8601" in data
    assert "dst" in data
    assert isinstance(data["dst"], bool)


def test_get_current_time_default_timezone():
    response = client.get("/v1/time/now")  # no timezone parameter
    assert response.status_code == 200
    data = response.json()

    assert "iso_8601" in data
    assert "dst" in data
    assert isinstance(data["dst"], bool)
