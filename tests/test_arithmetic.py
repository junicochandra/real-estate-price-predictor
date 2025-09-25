from app.adapters.handlers import arithmetic_handler as controller
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


# Integration test for /arithmetic/add endpoint
def test_add_endpoint():
    response = client.get("/arithmetic/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_minus_endpoint():
    response = client.get('/arithmetic/minus?a=5&b=3')
    assert response.status_code == 200
    assert response.json() == {"result": 2}


def test_multiply_endpoint():
    response = client.get('/arithmetic/multiply?a=4&b=3')
    assert response.status_code == 200
    assert response.json() == {"result": 12}


def test_divide_endpoint():
    response = client.get('/arithmetic/divide?a=10&b=2')
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_divide_by_zero_endpoint():
    response = client.get('/arithmetic/divide?a=10&b=0')
    assert response.status_code == 200
    assert response.json() == {"error": "Division by zero is not allowed."}


# Unit tests for arithmetic_controller functions
def add_numbers():
    result = controller.add_numbers(2, 3)
    assert result == {"result": 5}


def subtract_numbers():
    result = controller.subtract_numbers(5, 3)
    assert result == {"result": 2}


def multiply_numbers():
    result = controller.multiply_numbers(4, 3)
    assert result == {"result": 12}


def divide_numbers():
    result = controller.divide_numbers(10, 2)
    assert result == {"result": 5.0}


def divide_by_zero():
    result = controller.divide_numbers(10, 0)
    assert result == {"error": "Division by zero is not allowed."}
