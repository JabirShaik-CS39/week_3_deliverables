from test_conftest import client
def test_create_task():

    login = client.post(
        "/auth/login",
        json={
            "email": "jabir@test.com",
            "password": "password123"
        }
    )

    token = login.json()["access_token"]

    response = client.post(
        "/tasks",
        headers={
            "Authorization":
            f"Bearer {token}"
        },
        json={
            "title": "Build Login API",
            "description": "JWT Auth",
            "project_id": 1,
            "assigned_to": 1
        }
    )

    assert response.status_code == 200