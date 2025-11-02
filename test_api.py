import requests
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com"

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["id", "name", "email"],
}

def test_users_status():
    r = requests.get(BASE_URL + "/users")
    assert r.status_code == 200

def test_user_schema():
    r = requests.get(BASE_URL + "/users/1")
    assert r.status_code == 200
    validate(r.json(), user_schema)
def test_users_response_time(config):
    response = requests.get(config["base_url"] + "/users")
    assert response.elapsed.total_seconds() < 2
import pytest

@pytest.mark.parametrize("user_id", [1,2,3,4])


def test_user_by_id(config, user_id):
    response = requests.get(config["base_url"] + f"/users/{user_id}")

    assert response.status_code == 200
