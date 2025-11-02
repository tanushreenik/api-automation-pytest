import json
import pytest

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def config(env):
    with open(f"config/{env}.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def users_data():
    import json
    with open("testdata/users.json") as f:
        return json.load(f)
