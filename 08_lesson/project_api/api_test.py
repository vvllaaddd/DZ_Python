import pytest
import requests


# Подставьте данные
TOKEN = ""
BASE_URL = ""
USER_ID = ""



HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

USERS_PAYLOAD = {USER_ID: "worker"}


@pytest.fixture(scope="session")
def headers():
    return HEADERS


@pytest.fixture
def project_id(headers):
    payload = {
        "title": "Autotest Project",
        "users": USERS_PAYLOAD
    }
    res = requests.post(
        BASE_URL,
        json=payload,
        headers=headers
    )
    if res.status_code != 201:
        pytest.fail(
            f"Failed to create project: {res.status_code} {res.text}"
        )
    pid = res.json().get("id")
    yield pid
    requests.put(
        f"{BASE_URL}/{pid}",
        json={"deleted": True},
        headers=headers
    )



def test_create_project_positive(headers):
    payload = {
        "title": "Test Create",
        "users": USERS_PAYLOAD
    }
    res = requests.post(
        BASE_URL,
        json=payload,
        headers=headers
    )
    assert res.status_code == 201, (
        f"Expected 201, got {res.status_code}: {res.text}"
    )
    data = res.json()
    assert "id" in data, (
        "Response JSON should contain 'id'"
    )


def test_create_project_negative_missing_title(headers):
    payload = {"users": USERS_PAYLOAD}
    res = requests.post(
        BASE_URL,
        json=payload,
        headers=headers
    )
    assert res.status_code == 400, (
        f"Expected 400 for missing title, got {res.status_code}"
    )



def test_update_project_positive(headers, project_id):
    new_title = "Updated Title"
    res = requests.put(
        f"{BASE_URL}/{project_id}",
        json={"title": new_title},
        headers=headers
    )
    assert res.status_code == 200, (
        f"Expected 200, got {res.status_code}: {res.text}"
    )
    get_res = requests.get(
        f"{BASE_URL}/{project_id}",
        headers=headers
    )
    assert get_res.status_code == 200, (
        f"GET failed: {get_res.status_code}"
    )
    assert get_res.json().get("title") == new_title, (
        "Title was not updated"
    )


def test_update_project_negative_invalid_id(headers):
    invalid_id = (
        "00000000-0000-0000-0000-000000000000"
    )
    res = requests.put(
        f"{BASE_URL}/{invalid_id}",
        json={"title": "Fail"},
        headers=headers
    )
    assert res.status_code == 404, (
        f"Expected 404 for invalid ID, got {res.status_code}"
    )



def test_get_project_positive(headers, project_id):
    res = requests.get(
        f"{BASE_URL}/{project_id}",
        headers=headers
    )
    assert res.status_code == 200, (
        f"Expected 200, got {res.status_code}: {res.text}"
    )
    data = res.json()
    assert data.get("id") == project_id, (
        "Returned project ID mismatch"
    )


def test_get_project_negative_not_found(headers):
    invalid_id = (
        "00000000-0000-0000-0000-000000000000"
    )
    res = requests.get(
        f"{BASE_URL}/{invalid_id}",
        headers=headers
    )
    assert res.status_code == 404, (
        f"Expected 404 for invalid ID, got {res.status_code}"
    )
