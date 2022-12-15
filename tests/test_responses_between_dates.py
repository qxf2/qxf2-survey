"""
Tests for survey API endpoint '/survey/admin/QElo_filter_response' that fetches all the user responses between two given dates 
Test API response for different date ranges
    - Date range within which all the test data is present
    - Date range 1 year prior to the date where test data is stored
    - Current date
    - Date range covers first week of test data
    - Date range covers first two weeks of test data
    - Date range from a week prior to the dates where test data is present ,to the week succeeding the last date which has the test date
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
RESPONSES_URL = urljoin(URL, "survey/admin/QElo_filter_response")

"""
Test Data:
 :respondent_id 1: Generous Giver ID
 :respondent_id 2: Stingy Taker ID
 :question_no 1: Help taken
 :question_no 2: Help Given
"""
TEST_DATA = [
            #Date range whithin which all the test data is present
            ({"start_date": "1970-01-01","end_date": "1970-01-16"}, [
            {"respondent_id": 1, "date": "1970-01-02", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": 1, "date": "1970-01-09", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": 1, "date": "1970-01-16", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": 2, "date": "1970-01-02", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": 2, "date": "1970-01-09", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": 2, "date": "1970-01-16", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": 2, "date": "1970-01-02", "question_no": 2, "answer": "Generous Giver"}, 
            ]),

            #Date range 1 year prior to the date where test data is stored
            ({"start_date": "1969-01-01","end_date": "1969-12-31"},[]),

            #Current date
            ({"start_date": str(date.today()),"end_date": str(date.today())},[]),

            #Date range covers first week of test data
            ({"start_date": "1969-12-29","end_date": "1970-01-02"},[
            {"respondent_id": 1, "date": "1970-01-02", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": 2, "date": "1970-01-02", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": 2, "date": "1970-01-02", "question_no": 2, "answer": "Generous Giver"}
            ]),

            #Date range covers first two weeks of test data
            ({"start_date": "1969-12-29","end_date": "1970-01-09"},[
            {"respondent_id": 1, "date": "1970-01-02", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": 2, "date": "1970-01-02", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": 2, "date": "1970-01-02", "question_no": 2, "answer": "Generous Giver"},
            {"respondent_id": 1, "date": "1970-01-09", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": 2, "date": "1970-01-09", "question_no": 1, "answer": "Generous Giver"}
            ]),

            #Date range from a week prior to the dates where test data is present,
            #to the week succeeding the last date which has the test date
            ({"start_date": "1969-12-23","end_date": "1970-01-23"},[
            {"respondent_id": 1, "date": "1970-01-02", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": 1, "date": "1970-01-09", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": 1, "date": "1970-01-16", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": 2, "date": "1970-01-02", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": 2, "date": "1970-01-09", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": 2, "date": "1970-01-16", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": 2, "date": "1970-01-02", "question_no": 2, "answer": "Generous Giver"},
            ])
            ]

@pytest.mark.parametrize("date_range,expected_response", TEST_DATA)
def test_data_between_dateranges(date_range,expected_response):
    "Test the response data recieved for different date ranges"    
    #Get the response from API
    response = requests.post(RESPONSES_URL, data = json.dumps(date_range), headers = {'User': API_KEY})
    response_data = response.json()
    #Compare the two response recieved with the actual response
    diff = [i for i in response_data + expected_response if i not in response_data or i not in expected_response]
    result = len(diff) == 0
    assert response.status_code == 200
    assert len(response_data) == len(expected_response)
    assert result == True,f'There are {len(diff)} differences:\n{diff}'
