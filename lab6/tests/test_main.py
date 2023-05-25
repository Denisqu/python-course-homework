# https://testdriven.io/blog/fastapi-crud/
# https://pytest-with-eric.com/pytest-advanced/pytest-fastapi-testing/

from fastapi.testclient import TestClient
from lab5.app.main import app
from fastapi import Depends, HTTPException, status, APIRouter, Response

client = TestClient(app)


def test_create_test():
    sample_payload = {
        "id_task": 1,
        "name": "abcd",
        "code": "code"
    }
    response = client.post("/api/tests", json=sample_payload)
    response_json = response.json()
    is_ok = True
    if not sample_payload['id_task'] == response_json['test']['id_task']\
        or not sample_payload['name'] == response_json['test']['name']\
        or not sample_payload['code'] == response_json['test']['code']:
        is_ok = False
    assert is_ok
    assert response.status_code == 201


def test_get_test():
    response = client.get("/api/tests/1")

    assert response.status_code == 200
    assert response.json() == {
        "status":"success",
        "test": {
            "id":1,
            "id_task":1,
            "name":'Tests for something #1',
            "code":'Code...'
        }
    }


def test_update_test():
    sample_payload = {
        "id": 2,
        "id_task":1,
        "name":"ChaNged_Name",
        "code":"new_code"
    }
    response = client.patch("/api/tests/2", json=sample_payload)
    assert response.json() == {
        "status": "success",
        "test": {
            "id": 2,
            "id_task": 1,
            "name": "ChaNged_Name",
            "code": "new_code"
        }
    }


def test_delete_test():
    response = client.delete("/api/tests/4")
    assert response.status_code == 204


