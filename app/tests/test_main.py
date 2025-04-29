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

def test_when_given_user_name_should_create_a_student_in_db(client):
    rand_value = randint(0, 100000)
    first_name = f"John {rand_value}"
    last_name = f"World {rand_value}"
    try: 
        create_response = client.post("/student/", json={
                                    "first_name": first_name,
                                    "last_name":last_name
                                    })
    except Exception as e:
        print (str(e))
    assert create_response.status_code == 200
    student_id = create_response.json()['id']
    assert student_id != None

def test_get_all_students_should_return_list_of_students(client):
    response = client.get("/students/")
    assert response.status_code==200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for student in data: 
        assert "id" in student
        assert "first_name" in student
        assert "last_name" in student