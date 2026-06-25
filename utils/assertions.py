class Assertions:
    """
    Reusable checks for API responses.
    Use these in every test instead of writing the same checks repeatedly.
    """

    @staticmethod
    def status_code_is(response, expected_code):
        """
        Check that the response status code matches what we expect.
        Example: assert status is 200 for a successful GET request.
        """
        actual = response.status_code
        assert actual == expected_code, (
            f"Expected status code {expected_code} but got {actual}. "
            f"Response body: {response.text}"
        )

    @staticmethod
    def response_has_field(response_json, field_name):
        """
        Check that a specific field exists in the response body.
        Example: check that the response contains an "id" field.
        """
        assert field_name in response_json, (
            f"Expected field '{field_name}' not found in response. "
            f"Response was: {response_json}"
        )

    @staticmethod
    def field_equals(response_json, field_name, expected_value):
        """
        Check that a specific field has the exact value we expect.
        Example: check that name equals "morpheus".
        """
        actual = response_json.get(field_name)
        assert actual == expected_value, (
            f"Expected '{field_name}' to be '{expected_value}' but got '{actual}'"
        )

    @staticmethod
    def response_is_not_empty(response_json):
        """
        Check that the response body is not empty.
        """
        assert response_json, "Response body should not be empty"

    @staticmethod
    def response_time_is_acceptable(response, max_seconds=3):
        """
        Check that the API responded within an acceptable time.
        This is a basic performance check.
        Example: response should arrive in under 3 seconds.
        """
        actual_seconds = response.elapsed.total_seconds()
        assert actual_seconds < max_seconds, (
            f"Response took {actual_seconds:.2f} seconds — "
            f"expected under {max_seconds} seconds"
        )

    @staticmethod
    def list_is_not_empty(response_json, list_field):
        """
        Check that a list field in the response contains items.
        Example: check that "data" array has at least one user.
        """
        items = response_json.get(list_field, [])
        assert len(items) > 0, (
            f"Expected '{list_field}' to contain items but it was empty"
        )
