from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_shorten_and_redirect():
    payload = {"url": "https://example.com"}
    r = client.post("/shorten", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert "short_url" in data and "code" in data and data["url"] == payload["url"]

    code = data["code"]
    r2 = client.get(f"/{code}")
    assert r2.url == payload["url"]

def test_not_found():
    r = client.get("/nonexistent")
    assert r.status_code == 404
