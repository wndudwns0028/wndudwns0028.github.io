import requests

BASE_URL = "http://127.0.0.1:5000"

def test_create_user():
    payload = {"username": "testuser", "email": "testuser@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"

def test_get_user():
    # Assuming user with ID 1 was created during test_create_user()
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"

if __name__ == "__main__":
    test_create_user()
    test_get_user()