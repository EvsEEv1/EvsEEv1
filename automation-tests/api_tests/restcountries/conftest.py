import pytest
import requests

@pytest.fixture(scope="session")
def api():
    session = requests.Session()
    yield session
    session.close()
    
    