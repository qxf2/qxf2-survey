"""
Tests for survey API endpoint '/survey/admin/techs_learnt_on_week' that fetches all the dates on which technology is learned and not learned 
Test API response for different dates
    - Date of the week on which technology is learned
    - Date of the week on which technology is not learned
"""
import os
import json
import requests
import pytest
from datetime import date
from urllib.parse import urljoin
from decouple import config

URL = config("URL")
API_KEY = config("API_KEY")

#Get the url for the API endpoint that fetches dates of the week on which technology is learned and not learned
RESPONSES_URL = urljoin(URL, "/survey/admin/techs_learnt_on_week")

"""
Test Data:
- Date of the week on which technology is learned
- Date of the week on which technology is not learned
"""
TEST_DATA = [
            
            #Date of the week on which technology learned
            ({"date": "1980-01-25"},
            [   
                {"Name": "Smart Learner","Technology": "__TEST__NEO4J"},
                {"Name": "Smart Learner","Technology": "__TEST__PYTHON"},
                {"Name": "Slow Learner","Technology": "__TEST__PYTHON"},
                {"Name": "Smart Learner","Technology": "__TEST__JAVA"},
                {"Name": "Smart Learner","Technology": "__TEST__RUST"}
]),
            #Date of the week on which technology not learned
            ({"date": "1980-01-01"},[])
]

@pytest.mark.parametrize("date,expected_response", TEST_DATA)
def test_technology_learnt(date,expected_response):
    "Test the response data recieved for date of the week on which technology is learned and not learned"    
    #Get the response from API
    response = requests.post(RESPONSES_URL, data = json.dumps(date), headers = {'User': API_KEY})
    response_data = response.json()
    #Compare the two response recieved with the actual response
    diff = [i for i in response_data + expected_response if i not in response_data or i not in expected_response]
    result = len(diff) == 0
    assert response.status_code == 200
    assert len(response_data) == len(expected_response)
    assert result == True,f'There are {len(diff)} differences:\n{diff}'
