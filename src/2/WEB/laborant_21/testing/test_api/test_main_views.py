from starlette.testclient import TestClient
from fastapi import status
from api.api_v1.books.crud import storage
import pytest

from main import app

def test_root_view(client):
    response = client.get('/')
    response_data = response.json()
    excepted_message = f'Hello, World!'

    assert response.status_code == status.HTTP_200_OK
    assert response_data['docs'] == '/docs'
    assert response_data['message'] == excepted_message

@pytest.mark.parametrize(
        'name',
        [
            'BGPU',
            'Denchik',
            'Artem',
            '',
            '-={"',
        ]
)
def test_root_view_custom_name(name: str, client):
    query = {'name': name}
    response = client.get('/', params=query)
    response_data = response.json()
    expected_message = f'Hello, {name}!'

    assert response.status_code == status.HTTP_200_OK
    assert response_data['docs'] == '/docs'
    assert response_data['message'] == expected_message
