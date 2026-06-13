from test_conftest import client

def test_create_project():

    login = client.post(
        "/auth/login",
        json={
            "email": "jabir@test.com",
            "password": "password123"
        }
    )

    token = login.json()["access_token"]

    response = client.post(
        "/projects",
        headers={
            "Authorization":
            f"Bearer {token}"
        },
        json={
            "name": "FastAPI Project",
            "shift_mode": "General"
        }
    )

    assert response.status_code == 200