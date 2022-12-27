"""
Tests for survey API endpoint '/survey/admin/QElo_filter_response' that fetches all the user responses between two given dates 
Test API response for different date ranges
    - Date range within which all the test data is present
    - Date range 1 year prior to the date where test data is stored
    - Current date
    - Date range covers first week of test data
    - Date range covers first two weeks of test data
    - Date range from a week prior to the dates where test data is present ,to the week succeeding the last date which has the test date
    - Date range that has response from an inactive user
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

#Get the url for the API endpoint that fetches user responses b/w two given dates
RESPONSES_URL = urljoin(URL, "/survey/admin/techs_learnt_on_week")

"""
Test Data:
 :respondent_id 1: Generous Giver ID
 :respondent_id 2: Generous Taker ID
 :question_no 1: Help taken
 :question_no 2: Help Given
"""
TEST_DATA = [
            
            #Date on which technology learned
            ({"date": "1980-01-25"},
            [   
                {"Name": "Smart Learner","Technology": "__TEST__NEO4J"},
                {"Name": "Smart Learner","Technology": "__TEST__PYTHON"},
                {"Name": "Slow Learner","Technology": "__TEST__PYTHON"},
                {"Name": "Smart Learner","Technology": "__TEST__JAVA"},
                {"Name": "Smart Learner","Technology": "__TEST__RUST"}
]),
            #Date on which technology not learned
            ({"date": "1980-01-01"},[])
]

@pytest.mark.parametrize("date,expected_response", TEST_DATA)
def test_technology_learnt(date,expected_response):
    "Test the response data recieved for different date ranges"    
    #Get the response from API
    response = requests.post(RESPONSES_URL, data = json.dumps(date), headers = {'User': API_KEY})
    response_data = response.json()
    #Compare the two response recieved with the actual response
    diff = [i for i in response_data + expected_response if i not in response_data or i not in expected_response]
    result = len(diff) == 0
    assert response.status_code == 200
    assert len(response_data) == len(expected_response)
    assert result == True,f'There are {len(diff)} differences:\n{diff}'
