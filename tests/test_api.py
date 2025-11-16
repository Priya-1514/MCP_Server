from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    r = client.get("/")
    assert r.status_code == 200

def test_price():
    r = client.get("/price/BTC")
    assert r.status_code == 200
    assert "price" in r.json()

def test_history():
    r = client.get("/history/BTC")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
