import requests
import pytest
pytestmark = pytest.mark.api
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_returns_list():
    r = requests.get(f"{BASE_URL}/posts", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]

def test_get_single_post():
    r = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert "title" in data

def test_create_post_returns_201_and_payload_echo():
    payload = {"title": "QA Test", "body": "Testing API", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    assert r.status_code == 201
    data = r.json()
    # JSONPlaceholder "фейковый" — но обычно возвращает назад поля
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
