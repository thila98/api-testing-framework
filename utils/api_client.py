import requests
from config.settings import BASE_URL, TIMEOUT, HEADERS


class APIClient:
    """
    A reusable API client for making HTTP requests.
    All tests use this instead of calling requests directly.
    """

    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT
        self.headers = HEADERS

    def get(self, endpoint, params=None):
        """
        Send a GET request — used to fetch/retrieve data.
        Example: GET /users/1 fetches user with ID 1
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
        return response

    def post(self, endpoint, body=None):
        """
        Send a POST request — used to create new data.
        Example: POST /users creates a new user
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=self.headers, json=body, timeout=self.timeout)
        return response

    def put(self, endpoint, body=None):
        """
        Send a PUT request — used to update existing data.
        Example: PUT /users/1 updates user with ID 1
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, headers=self.headers, json=body, timeout=self.timeout)
        return response

    def delete(self, endpoint):
        """
        Send a DELETE request — used to remove data.
        Example: DELETE /users/1 deletes user with ID 1
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=self.headers, timeout=self.timeout)
        return response
