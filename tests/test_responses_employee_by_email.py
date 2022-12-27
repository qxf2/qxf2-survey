"""
Tests for survey API endpoint '/survey/admin/get_employee_by_email' that fetches employees by email
Test API response for 
    - endpoint by passing an email that exists in the database and validate the response data
    - endpoint by passing an email that does not exist in database and validate the response
   
"""
import os
import json
import requests
import pytest
from datetime import date
from urllib.parse import urljoin
from decouple import config

URL = "http://127.0.0.1:8000"
API_KEY = config("API_KEY")

#Get the url for the API endpoint that fetches user responses between two given dates
RESPONSES_URL = urljoin(URL, "survey/admin/get_employee_by_email")

"""
Test Data:
 :author_name : author name
 :lastName: last name of the employee
 :firstName: firstname of the employee
 :ID : employee ID
 :email: employee email ID
 :status: status
"""
TEST_DATA = [
            # passing an email that exists in the database and validate the response data
            ({"email": "generoustaker@qxf2.com"}, [
            {"employee_details": {"author_name": "Generous Taker", "firstName": "Generous", "lastName": "Taker", "fullName": "Generous Taker","ID":2,"email":"generoustaker@qxf2.com","status":"Y"}},
            ]),   
            # passing an email that exists in the database and validate the response data
            ({"email": "generousgiver@qxf2.com"}, [
            {"employee_details": {"author_name": "Generous Giver", "firstName": "Generous", "lastName": "Giver", "fullName": "Generous Giver","ID":1,"email":"generousgiver@qxf2.com","status":"Y"}},
            ]),                   
            # passing an email that does not exist in database and validate the response 
            ({"email": "generoustake@qxf2.com"}, 
            "Employee does not exist"
            )]

@pytest.mark.parametrize("email,expected_response", TEST_DATA)
def test_get_employee_by_email(email,expected_response):
    "Test the response details for given email"    
    #Get the response from API
    response = requests.post(RESPONSES_URL, data = json.dumps(email), headers = {'User': API_KEY})
    response_data = response.json()
    print ("response_data",response_data)
    #Compare the two response recieved with the actual response    
    assert (response_data) == (expected_response)    
