"""
Tests for survey API endpoint '/survey/admin/QElo_filter_technology'
    - Endpoint that fetches all tech responses, between the date range passed
Test cases:
    1. Date range one year prior the the dates where data exists
    2. Date range that covers all three weeks of existing data
    3. Date range that covers only first  week of existing data
    4. Date range that covers only first two weeks of existing data
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

#Construct URL for API endpoint that fetches tech responses between two given dates
REQUEST_URL = urljoin(URL, "/survey/admin/QElo_filter_technology")

"""
Test Data:
 :respondent_id 4: Smart Learner ID
 :respondent_id 5: Slow Learner ID
"""
TEST_DATA = [
            #1. Date range one year prior the the dates where data exists
            ({"start_date": "1979-01-01", "end_date": "1979-01-31"}, []),

            #2. Date range that covers all three weeks of existing data
            ({"start_date": "1980-01-11","end_date": "1980-01-25"},
            [
            {
                "respondent_id": 4,
                "technology": "__TEST__NEO4J",
                "date": "1980-01-25"
            },
            {
                "respondent_id": 4,
                "technology": "__TEST__PYTHON",
                "date": "1980-01-25"
            },
            {
                "respondent_id": 5,
                "technology": "__TEST__PYTHON",
                "date": "1980-01-25"
            },
            {
                "respondent_id": 4,
                "technology": "__TEST__JAVA",
                "date": "1980-01-25"
            },
            {
                "respondent_id": 4,
                "technology": "__TEST__RUST",
                "date": "1980-01-25"
            },
            {
                "respondent_id": 4,
                "technology": "__TEST__PYTHON",
                "date": "1980-01-11"
            },
            {
                "respondent_id": 4,
                "technology": "__TEST__JAVA",
                "date": "1980-01-11"
            },
            {
                "respondent_id": 4,
                "technology": "__TEST__PYTHON",
                "date": "1980-01-18"
            },
            {
                "respondent_id": 5,
                "technology": "__TEST__PYTHON",
                "date": "1980-01-18"
            },
            {
                "respondent_id": 4,
                "technology": "__TEST__JAVA",
                "date": "1980-01-18"
            },
            {
                "respondent_id": 4,
                "technology": "__TEST__RUST",
                "date": "1980-01-18"
            }]),


            #3. Date range that covers only first  week of existing data
            #(),

            #4. Date range that covers only first two weeks of existing data
            #()
            ]

@pytest.mark.parametrize("date_range,expected_response", TEST_DATA)
def test_data_between_dateranges(date_range,expected_response):
    "Test the response data recieved for different date ranges"
    #Get the response from API
    response = requests.post(REQUEST_URL, data = json.dumps(date_range), headers = {'User': API_KEY})
    response_data = response.json()
    #Compare the two response recieved with the actual response
    diff = [i for i in response_data + expected_response if i not in response_data or i not in expected_response]
    result = len(diff) == 0
    assert response.status_code == 200
    assert len(response_data) == len(expected_response)
    assert result == True,f'There are {len(diff)} differences:\n{diff}'
