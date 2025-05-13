from fastapi.testclient import TestClient
import pytest
from app import chatbot_app

client = TestClient(chatbot_app)

def test_add_endpoint():
    """Test the /add endpoint with various inputs"""
    response = client.post("/add", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}
    
    response = client.post("/add", params={"a": -1, "b": 1})
    assert response.status_code == 200
    assert response.json() == {"result": 0}
    
    response = client.post("/add", params={"a": 0, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"result": 0}

def test_sub_endpoint():
    """Test the /sub endpoint with various inputs"""
    response = client.post("/sub", params={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}
    
    response = client.post("/sub", params={"a": 3, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 0}
    
    response = client.post("/sub", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": -1}

def test_mul_endpoint():
    """Test the /mul endpoint with various inputs"""
    response = client.post("/mul", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6}
    
    response = client.post("/mul", params={"a": -1, "b": 1})
    assert response.status_code == 200
    assert response.json() == {"result": -1}
    
    response = client.post("/mul", params={"a": -1, "b": -1})
    assert response.status_code == 200
    assert response.json() == {"result": 1}

    response = client.post("/mul", params={"a": 2, "b": -1})
    assert response.status_code == 200
    assert response.json() == {"result": -2}
