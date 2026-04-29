from collections.abc import Generator

import pytest
from starlette.testclient import TestClient

from main import app

@pytest.fixture()
def client() -> Generator[TestClient]:
    with TestClient(app=app) as client:
        yield client