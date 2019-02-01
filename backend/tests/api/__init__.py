from entry import create_db, drop_db, setup_config
import pytest

@pytest.fixture
def client(scope='module'):
    app = setup_config(testing=True)
    client = app.test_client()
    yield client
    drop_db(app)
