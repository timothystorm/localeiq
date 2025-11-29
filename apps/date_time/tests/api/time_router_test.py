from fastapi.testclient import TestClient

from date_time.main import app

client = TestClient(app)


def test_fetch_current_time():
    response = client.post("/v1/time", json={"timezone": "America/Denver"})
    assert response.status_code == 200
    data = response.json()

    assert "iso_8601" in data
    assert "dst" in data
    assert isinstance(data["dst"], bool)
