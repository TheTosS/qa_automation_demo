import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_create_post():
    payload = {"title": "QA Test", "body": "Testing API", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "QA Test"
