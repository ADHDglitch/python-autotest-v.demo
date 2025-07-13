import requests

def test_get_post_by_id():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    assert "userId" in data, "userId not found in response"
    assert data["id"] == 1, f"Expected id to be 1, got {data['id']}"
