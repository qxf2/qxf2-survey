"""
Tests for survey API delete endpoint '/survey/admin/employees/{id}' that deletes the employee record with id mentioned in request
Test API response for when
- ID of user that exists in database is passed
- ID of user that does not exist in database is passed
Note: using the same ID for both scenarios here, because, after 1st scenario, the ID of the user gets deleted from the database.

"""
import os
import json
import requests
import pytest
from urllib.parse import urljoin
from decouple import config

URL = config("URL")
API_KEY = config("API_KEY")

#Get the url for the API endpoint that fetches user responses b/w two given dates
RESPONSES_URL = urljoin(URL, "/survey/admin/employees")

"""
Test Data:
 existing_id : 7 
 Non-existing id : 7
"""
TEST_DATA = [
            # the ID of the user to be deleted passed
            ("7", {"msg": "Successfully deleted employee with id 7"},200),

            # the ID that does not exist passed
            ("7",{"msg": "Employee not found"},404)
            ]

@pytest.mark.parametrize("employee_id,expected_response,expected_status_code", TEST_DATA)
def test_employee_delete_endpoint(employee_id,expected_response,expected_status_code):
    "Test the response data received for the employee delete endpoint with existing and non-existing employee ID"    
    #Get the response from API
    response = requests.delete(RESPONSES_URL+ "/" + employee_id, headers = {'User': API_KEY})
    response_data = response.json()
    assert response_data == expected_response
    assert response.status_code == expected_status_code
