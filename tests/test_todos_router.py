from urllib import response
from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_pytest06')        
from main import app

client = TestClient(app)

def test_post_to_insert(db):
    response = client.post(
        "/",
        json={
            "name": "string",
            "description": "string",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "string"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_put_update(db):
    response = client.put(
        "/620b069f392a8f675d7fcce8",
        json={
            "name": "update",
            "description": "string",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "update"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_todo_delete(db):
    response = client.delete(
        "/620b069f392a8f675d7fcce8"
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}