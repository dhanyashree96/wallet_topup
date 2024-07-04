from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_topup():
    response = client.post("/topup", json={"user_id": "testuser", "amount": 100.0})
    assert response.status_code == 200
    assert response.json()["new_balance"] == 100.0

def test_deduct():
    response = client.post("/deduct", json={"user_id": "testuser", "amount": 50.0})
    assert response.status_code == 200
    assert response.json()["new_balance"] == 50.0

def test_get_balance():
    response = client.get("/balance", params={"user_id": "testuser"})
    assert response.status_code == 200
    assert response.json()["balance"] == 50.0
