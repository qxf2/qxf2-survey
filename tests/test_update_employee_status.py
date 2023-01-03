"""
Test for survey API endpoint `/survey/admin/update_employee_status`.
The endpoint is used to update the status of an employee.
Employee status can either be 'Y' or 'N'
The following test is covered:
1. Update the status of an inactive user to active
2. Use the `/survey/admin/get_employee_by_email` to get employee employee details and make sure the employee status has changed
3. Change the status of employee back to inactive
4. Repeat step 2
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

#Get the url to update employee status
UPDATE_STATUS_URL = urljoin(URL, "/survey/admin/update_employee_status")

#Get the url to get employee details by passing employee email
EMPLOYEE_INFO_URL = urljoin(URL, "/survey/admin/get_employee_by_email")

TEST_DATA = [
    #Data to set employee status to active
    ({"email":{"email":"user_status_to_be_updated@qxf2.com"},"status":{"employee_status":"Y"}},
    #Expected response to check if employee status is set to 'Y'
    [{"employee_details": {"firstName": "Update", "lastName": "My Status", 
    "fullName": "Update My Status", "ID": 8, "email": "user_status_to_be_updated@qxf2.com","status": "Y"}}],
    #Response message
    ["Successfully updated status of employee with email user_status_to_be_updated@qxf2.com"]),

    #Data to set employee status to inactive
    ({"email":{"email":"user_status_to_be_updated@qxf2.com"},"status":{"employee_status":"N"}},
    #Expected response to check if employee status is set to 'N'
    [{"employee_details": {"firstName": "Update", "lastName": "My Status", 
    "fullName": "Update My Status", "ID": 8, "email": "user_status_to_be_updated@qxf2.com","status": "N"}}],
    #Response message
    ["Successfully updated status of employee with email user_status_to_be_updated@qxf2.com"]),

    #Data to set employee status of an user that does not exist in database
    ({"email":{"email":"user_that_does_not_exist@qxf2.com"},"status":{"employee_status":"N"}},
    #Expected response to check if we get appropriate error message
    "Employee does not exist",
    #check for appropriate response message
    "Employee does not exist")]



@pytest.mark.parametrize("update_status_data, expected_response, response_msg", TEST_DATA)
def test_update_employee_status(update_status_data,expected_response,response_msg):
    "Used to update employee status and validate result"
    #Update employee status
    update_status = requests.post(UPDATE_STATUS_URL, data = json.dumps(update_status_data), headers = {'User': API_KEY})
    update_msg = update_status.json()

    
    #Get employee details
    employee_details = get_employee_details(update_status_data)
    
    if update_status_data['email']['email'] != "user_that_does_not_exist@qxf2.com":
        #Compare the actual response with the expected response
        response_diff = [i for i in employee_details + expected_response if i not in employee_details or i not in expected_response]
        response_result = len(response_diff) == 0
        assert len(employee_details) == len(expected_response)
        assert response_result == True,f'There are {len(response_diff)} differences:\n{response_diff}'
    else:
        assert employee_details == expected_response
    assert update_msg == response_msg



def get_employee_details(update_status_data):
    "Used to get information about an employee by passing the empoyees email"
    email_data = {"email": f"{update_status_data['email']['email']}"}
    employee_details = requests.post(EMPLOYEE_INFO_URL, data = json.dumps(email_data), headers = {'User': API_KEY}).json()
    return employee_details