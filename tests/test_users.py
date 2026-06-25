import pytest
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils.api_client import APIClient
from utils.assertions import Assertions

# Load test data from our JSON file
with open("config/test_data.json") as f:
    data = json.load(f)

# Create one API client used by all tests
client = APIClient()
assert_that = Assertions()


# ─────────────────────────────────────────
# GET TESTS — fetching data
# ─────────────────────────────────────────

def test_get_all_users_returns_200():
    """
    TC_001 - Functional
    Verify that GET /users returns a 200 status code
    """
    response = client.get("/users", params={"page": data["valid_page"]})
    Assertions.status_code_is(response, 200)


def test_get_all_users_returns_list_of_users():
    """
    TC_002 - Functional
    Verify that GET /users returns a list of users in the data field
    """
    response = client.get("/users", params={"page": 1})
    body = response.json()
    Assertions.response_has_field(body, "data")
    Assertions.list_is_not_empty(body, "data")


def test_get_all_users_response_has_pagination_fields():
    """
    TC_003 - Functional
    Verify that GET /users response includes pagination info
    """
    response = client.get("/users", params={"page": 1})
    body = response.json()
    Assertions.response_has_field(body, "page")
    Assertions.response_has_field(body, "total")
    Assertions.response_has_field(body, "per_page")


def test_get_single_user_returns_200():
    """
    TC_004 - Functional
    Verify that GET /users/{id} returns 200 for a valid user
    """
    response = client.get(f"/users/{data['valid_user_id']}")
    Assertions.status_code_is(response, 200)


def test_get_single_user_returns_correct_fields():
    """
    TC_005 - Functional
    Verify that a single user response has id, email, first_name, last_name
    """
    response = client.get(f"/users/{data['valid_user_id']}")
    body = response.json()
    user = body.get("data", {})
    Assertions.response_has_field(user, "id")
    Assertions.response_has_field(user, "email")
    Assertions.response_has_field(user, "first_name")
    Assertions.response_has_field(user, "last_name")


def test_get_single_user_returns_correct_id():
    """
    TC_006 - Functional
    Verify that the returned user ID matches the requested ID
    """
    user_id = data["valid_user_id"]
    response = client.get(f"/users/{user_id}")
    body = response.json()
    Assertions.field_equals(body["data"], "id", user_id)


def test_get_users_response_time_is_acceptable():
    """
    TC_007 - Performance
    Verify that GET /users responds within 3 seconds
    """
    response = client.get("/users")
    Assertions.response_time_is_acceptable(response, max_seconds=3)


# ─────────────────────────────────────────
# POST TESTS — creating data
# ─────────────────────────────────────────

def test_post_create_user_returns_201():
    """
    TC_008 - Functional
    Verify that POST /users returns 201 Created
    """
    response = client.post("/users", body=data["valid_user"])
    Assertions.status_code_is(response, 201)


def test_post_create_user_returns_correct_name():
    """
    TC_009 - Functional
    Verify that the created user has the name we sent
    """
    response = client.post("/users", body=data["valid_user"])
    body = response.json()
    Assertions.field_equals(body, "name", data["valid_user"]["name"])


def test_post_create_user_returns_id():
    """
    TC_010 - Functional
    Verify that the created user gets an ID assigned
    """
    response = client.post("/users", body=data["valid_user"])
    body = response.json()
    Assertions.response_has_field(body, "id")


def test_post_create_user_returns_created_at():
    """
    TC_011 - Functional
    Verify that the created user has a createdAt timestamp
    """
    response = client.post("/users", body=data["valid_user"])
    body = response.json()
    Assertions.response_has_field(body, "createdAt")


# ─────────────────────────────────────────
# PUT TESTS — updating data
# ─────────────────────────────────────────

def test_put_update_user_returns_200():
    """
    TC_012 - Functional
    Verify that PUT /users/{id} returns 200
    """
    response = client.put(f"/users/{data['valid_user_id']}", body=data["updated_user"])
    Assertions.status_code_is(response, 200)


def test_put_update_user_returns_updated_job():
    """
    TC_013 - Functional
    Verify that the updated user has the new job title
    """
    response = client.put(f"/users/{data['valid_user_id']}", body=data["updated_user"])
    body = response.json()
    Assertions.field_equals(body, "job", data["updated_user"]["job"])


def test_put_update_user_returns_updated_at():
    """
    TC_014 - Functional
    Verify that the updated user has an updatedAt timestamp
    """
    response = client.put(f"/users/{data['valid_user_id']}", body=data["updated_user"])
    body = response.json()
    Assertions.response_has_field(body, "updatedAt")


# ─────────────────────────────────────────
# DELETE TESTS — removing data
# ─────────────────────────────────────────

def test_delete_user_returns_204():
    """
    TC_015 - Functional
    Verify that DELETE /users/{id} returns 204 No Content
    """
    response = client.delete(f"/users/{data['valid_user_id']}")
    Assertions.status_code_is(response, 204)


def test_delete_user_returns_empty_body():
    """
    TC_016 - Functional
    Verify that DELETE response has no body (204 means no content)
    """
    response = client.delete(f"/users/{data['valid_user_id']}")
    assert response.text == "", "DELETE response body should be empty"
