import pytest
import requests

API_KEY = "rc_live_ce2351459f984e228024a777fe78e85a"

@pytest.fixture(scope="session")
def api():
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {API_KEY}"})
    yield session
    session.close()
    
    