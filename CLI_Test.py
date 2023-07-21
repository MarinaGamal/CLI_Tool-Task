import requests
import pytest

# API endpoint URLs
base_url = "https://reqres.in/api"
create_user_url = f"{base_url}/users"
list_users_url = f"{base_url}/users"

user_id = None


def validate_date_format(date_str):
    try:
        from datetime import datetime
        datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        return True
    except ValueError:
        return False


# Test case for user creation
def test_create_user():
    global user_id

    # Test data
    payload = {
        "name": "Marina",
        "job": "Software Engineer"
    }

    # Send POST request to create user
    response = requests.post(create_user_url, json=payload)

    # Verify the response
    assert response.status_code == 201
    assert response.json()["name"] == "Marina"
    assert response.json()["job"] == "Software Engineer"
    assert "createdAt" in response.json()

    created_at = response.json()["createdAt"]

    # Extract the user ID for subsequent test cases
    user_id = response.json()["id"]

    # Update the URLs with the user_id
    global update_user_url, delete_user_url
    update_user_url = f"{base_url}/users/{user_id}"
    delete_user_url = f"{base_url}/users/{user_id}"

    assert validate_date_format(created_at)


# Test case for listing users
def test_list_users():
    # Send GET request to list users
    response = requests.get(list_users_url)

    # Verify the response
    assert response.status_code == 200

    # Assert fields for each user entry in the data list
    data = response.json()["data"]
    assert isinstance(data, list)  # Ensure data is a list
    assert len(data) > 0  # Check if there is at least one user entry as I already created one

    for user in data:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user


# Test case for updating a user
def test_update_user():
    # Test data
    payload = {
        "name": "Marina Gamal",
        "job": "QA Software Engineer"
    }

    # Send PUT request to update user
    response = requests.put(update_user_url, json=payload)

    # Verify the response
    assert response.status_code == 200
    assert response.json()["name"] == "Marina Gamal"
    assert response.json()["job"] == "QA Software Engineer"

    assert "updatedAt" in response.json()  # Check for the presence of the updatedAt field
    updated_at = response.json()["updatedAt"]
    assert validate_date_format(updated_at)



# Test case for deleting a user
def test_delete_user():
    # Send DELETE request to delete user
    response = requests.delete(delete_user_url)

    # Verify the response
    assert response.status_code == 204  

# Test case for user creation failure
def test_create_user_failure():
    # Test data with missing required field
    payload = {
        "job": "Software Engineer"
    }

    # Send POST request to create user
    response = requests.post(create_user_url, json=payload)

    # Verify the response
    assert response.status_code == 400  

# Test case for listing users failure
def test_list_users_failure():
    # Send GET request to a non-existent endpoint
    response = requests.get(base_url + "/nonexistent")

    # Verify the response
    assert response.status_code == 404 
	
# Test case for updating a user failure
def test_update_user_failure():
    # Test data with missing required field
    payload = {
        "job": "QA Software Engineer"
    }

    # Send PUT request to update user
    response = requests.put(update_user_url, json=payload)

    # Verify the response
    assert response.status_code == 400
	
# Test case for deleting a user failure
def test_delete_user_failure():
    # Send DELETE request to delete user (non-existent user_id)
    response = requests.delete(f"{base_url}/users/9999")

    # Verify the response
    assert response.status_code == 404

# Execute the test cases
if __name__ == "__main__":
    pytest.main([__file__, "--html=report.html"])
