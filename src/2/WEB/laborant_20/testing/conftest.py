from os import getenv

import pytest

from api.api_v1.books.dependencies import UNSAFE_METHODS

if getenv('TESTING') != '1':
    pytest.exit('Environment is not reaty for test')