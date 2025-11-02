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
