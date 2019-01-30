import pytest

from entry import setup_config

@pytest.fixture
def client():
    client = setup_config(testing=True).test_client()
    yield client