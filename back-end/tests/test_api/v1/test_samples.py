from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_read_samples():
    response = client.get("/api/v1/samples/")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["data"]) == 2
    assert data["data"][0]["title"] == "Sample 1"

def test_list_samples_paginated():
    response = client.get("/api/v1/samples/list?page=1&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["data"]["items"]) == 5
    assert data["data"]["total"] == 50
    assert data["data"]["page"] == 1
    assert data["data"]["limit"] == 5
    assert data["data"]["total_pages"] == 10
