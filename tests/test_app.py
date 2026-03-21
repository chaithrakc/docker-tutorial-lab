from fastapi.testclient import TestClient
from app import create_app
from app.config import Config
import pytest

@pytest.fixture
def client():
    test_config = Config()
    test_config.MODEL_PATH = "models/test_model.pkl"
    app = create_app(test_config)

    with TestClient(app) as client:
        yield client

def test_home(client):
    """Test the home endpoint to ensure it returns the expected welcome message."""
    response = client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Welcome to the Bank Note Authentication API" in data["message"]