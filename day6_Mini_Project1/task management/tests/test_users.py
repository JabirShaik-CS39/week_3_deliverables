from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_current_user():

    login = client.post(
        "/auth/login",
        json={
            "email": "jabir@test.com",
            "password": "password123"
        }
    )

    token = login.json()["access_token"]

    response = client.get(
        "/users/me",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    assert response.status_code == 200