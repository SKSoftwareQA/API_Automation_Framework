import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestAPIRequests:

    def test_get_request(self, api_request_context):
        """Test GET request to fetch a post"""
        response = api_request_context.get(f"{BASE_URL}/posts/1")

        assert response.status == 200
        assert response.ok

        response_data = response.json()
        assert response_data["id"] == 1
        assert response_data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

    def test_post_request(self, api_request_context):
        """Test POST request to create a new post"""
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }

        response = api_request_context.post(
            f"{BASE_URL}/posts",
            data=payload
        )

        assert response.status == 201
        assert response.ok

        response_data = response.json()
        assert response_data["id"] == 101
        assert response_data["title"] == "foo"

    def test_put_request(self, api_request_context):
        """Test PUT request to update a post"""
        payload = {"title": "cool"}

        response = api_request_context.put(
            f"{BASE_URL}/posts/1",
            data=payload
        )

        assert response.status == 200

        response_data = response.json()
        assert response_data["title"] == "cool"

    def test_delete_request(self, api_request_context):
        """Test DELETE request to remove a post"""
        response = api_request_context.delete(f"{BASE_URL}/posts/1")

        assert response.status == 200
        assert response.ok
        assert response.json() == {}
        