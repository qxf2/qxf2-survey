"""
Test for /survey/admin/new_employee endpoint.
The test is used to add new employee to the database
The following test is covered:
1. Add a new employee
2. Make sure employee has been added by getting the employee details via /survey/admin/get_employee_by_email endpoint
3. The employee ID of the newly added employee is <Previous_id + 1>
4. If empty data is passed to the endpoint to /survey/admin/new_employee, make sure we get error message
"""

import os
import json
import requests
import pytest
from datetime import datetime , timedelta, date
from dateutil.relativedelta import relativedelta, FR
from urllib.parse import urljoin
from decouple import config

URL = config("URL")
API_KEY = config("API_KEY")

#Get the url to add new employee
ADD_EMPLOYEE_URL = urljoin(URL, "/survey/admin/new_employee")

#Get the url to get employee details by passing employee email
EMPLOYEE_INFO_URL = urljoin(URL, "/survey/admin/get_employee_by_email")

TEST_DATA = [
    #Add employee with valid data
    ({"data":{"firstName":"New","lastName":"Added Employee","email":"newly_added_employee@qxf2.com",
    "fullName":"New Added Employee","status":"Y"}},
    #Expected response should contain details of employee added 
    [{"employee_details": {"firstName": "New", "lastName": "Added Employee", 
    "fullName": "New Added Employee", "ID": 9, "email": "newly_added_employee@qxf2.com","status": "Y"}}]),
    #Add employee with empty data
    ({},
    #Verify if the response shows failure message
    {"detail": [{"loc": ["body","data"],"msg": "field required","type": "value_error.missing"}]})
    ]

@pytest.mark.parametrize("add_employee_data,expected_response", TEST_DATA)
def test_add_new_employee(add_employee_data, expected_response):
    "Used to add new employee and validate the result"
    
    add_employee = requests.post(ADD_EMPLOYEE_URL, data = json.dumps(add_employee_data), headers = {'User': API_KEY}).json()
    
    employee_details = [add_employee]
    #If the data submitted to create employee is valid then get the employee details and compare with expected response
    if 'data' in add_employee_data:       
        employee_details = get_employee_details(add_employee_data)
 
        #Compare the actual response with the expected response
        response_diff = compare_responses(employee_details,expected_response)
        response_result = len(response_diff) == 0

        assert add_employee == {"msg": "Successfully registered new employee"}
        assert len(employee_details) == len(expected_response)
        assert response_result == True,f'There are {len(response_diff)} differences:\n{response_diff}'
    #If the data submitted to create employee is empty or invalid, check is we get appropriate error message
    else:
        assert add_employee == expected_response

def get_employee_details(add_employee_data):
    "Used to get information about an employee by passing the empoyees email"
    email_data = {"email": f"{add_employee_data['data']['email']}"}
    employee_details = requests.post(EMPLOYEE_INFO_URL, data = json.dumps(email_data), headers = {'User': API_KEY}).json()
    return employee_details

def compare_responses(response_data,expected_response):
    "Used to compare the expected response with the actual response"
    response_diff = [i for i in response_data + expected_response if i not in response_data or i not in expected_response]
    return response_diff
