from security import hash_password, verify_password

USER = {"username": "student", "email": "student@example.com", "password": "secret123"}


def test_password_hash():
    hashed = hash_password(USER["password"])
    assert hashed != USER["password"]
    assert verify_password(USER["password"], hashed)
    assert not verify_password("wrong", hashed)


def test_login_and_profile(client):
    registered = client.post("/auth/register", json=USER)
    assert registered.status_code == 201
    assert set(registered.json()) == {"id", "username", "email"}
    login = client.post("/auth/login", json=USER)
    assert login.status_code == 200
    token = login.json()["access_token"]
    profile = client.get("/profile/me", headers={"Authorization": f"Bearer {token}"})
    assert profile.status_code == 200
    assert profile.json() == registered.json()


def test_profile_requires_token(client):
    response = client.get("/profile/me")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}


def test_duplicate_registration(client):
    response1 = client.post("/auth/register", json=USER)
    assert response1.status_code == 201
    response2 = client.post("/auth/register", json=USER)
    assert response2.status_code == 409
    assert response2.json() == {"detail": "Email already registered"}


def test_wrong_password_login(client):
    client.post("/auth/register", json=USER)
    bad_login = {"email": USER["email"], "password": "incorrectpassword"}
    response = client.post("/auth/login", json=bad_login)
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid email or password"}


def test_invalid_registration_data(client):
    invalid_user = {"username": "bob", "email": "bob@example.com", "password": "123"}
    response = client.post("/auth/register", json=invalid_user)
    assert response.status_code == 422
