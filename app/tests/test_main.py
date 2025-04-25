import pytest
from fastapi.testclient import TestClient
from random import randint

# app->main.py is what app points to.
from app.main import app

#__init__.py establishes module
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_when_app_running_status_endpoint_should_return_OK(client):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "OK"