from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_item():
    response = client.post("/items", json={"id": 1, "name": "Test", "price": 10.5, "in_stock": True})
    assert response.status_code == 200

    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test"

def test_update_item():
    client.post("/items", json={"id": 2, "name": "Old", "price": 5.0, "in_stock": False})
    response = client.put("/items/2", json={"id": 2, "name": "New", "price": 15.0, "in_stock": True})
    assert response.status_code == 200
    assert response.json()["name"] == "New"

def test_delete_item():
    client.post("/items", json={"id": 3, "name": "ToDelete", "price": 1.0, "in_stock": True})
    response = client.delete("/items/3")
    assert response.status_code == 200