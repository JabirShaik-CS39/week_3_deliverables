from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_register_user():

    response = client.post(
        "/auth/register",
        json={
            "name": "Jabir",
            "email": "jabir@test.com",
            "password": "password123",
            "mobile": "9876543210"
        }
    )

    assert response.status_code in [200, 201]