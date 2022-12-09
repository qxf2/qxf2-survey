"""
Tests for survey API endpoint that fetches all the user responses between two given dates 
Test API response for different date ranges
    - Date range whithin which all the test data is present
    - Date range 1 year prior to the date where test data is stored
    - Current date
    - Date range covers first week of test data
    - Date range covers first two weeks of test data
    - Date range from a week prior to the dates where test data is present ,to the week succeeding the last date which has the test date
"""
import json
import os
import pytest
from unittest.mock import patch
import requests
from decouple import config
from urllib.parse import urljoin
from datetime import date

URL = config("URL")
API_KEY = config("API_KEY")

TEST_DATA = [
            #Date range whithin which all the test data is present
            ({"start_date": "1970-01-01","end_date": "1970-01-16"}, [
            {"respondent_id": "Generous Giver ID", "date": "1970-01-02", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": "Generous Giver ID", "date": "1970-01-09", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": "Generous Giver ID", "date": "1970-01-16", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-02", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-09", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-16", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-02", "question_no": 2, "answer": "Generous Giver"}, 
            ]),

            #Date range 1 year prior to the date where test data is stored
            ({"start_date": "1969-01-01","end_date": "1969-12-31"},[]),

            #Current date
            ({"start_date": str(date.today()),"end_date": str(date.today())},[]),

            #Date range covers first week of test data
            ({"start_date": "1969-12-29","end_date": "1970-01-02"},[
            {"respondent_id": "Generous Giver ID", "date": "1970-01-02", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-02", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-02", "question_no": 2, "answer": "Generous Giver"}
            ]),

            #Date range covers first two weeks of test data
            ({"start_date": "1969-12-29","end_date": "1970-01-09"},[
            {"respondent_id": "Generous Giver ID", "date": "1970-01-02", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-02", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-02", "question_no": 2, "answer": "Generous Giver"},
            {"respondent_id": "Generous Giver ID", "date": "1970-01-09", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-09", "question_no": 1, "answer": "Generous Giver"}
            ]),

            #Date range from a week prior to the dates where test data is present ,to the week succeeding the last date which has the test date
            ({"start_date": "1969-12-23","end_date": "1970-01-23"},[
            {"respondent_id": "Generous Giver ID", "date": "1970-01-02", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": "Generous Giver ID", "date": "1970-01-09", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": "Generous Giver ID", "date": "1970-01-16", "question_no": 2, "answer": "Stingy Taker"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-02", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-09", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-16", "question_no": 1, "answer": "Generous Giver"},
            {"respondent_id": "Stingy Taker ID", "date": "1970-01-02", "question_no": 2, "answer": "Generous Giver"},
            ])
            ]


@pytest.mark.parametrize("date_range,expected_response", TEST_DATA)
def test_data_between_dateranges(date_range,expected_response):
    "Test the response data recieved for different date ranges"
    #Get the url for the API endpoint that fetches user responses b/w two given dates
    responses_api = "survey/admin/QElo_filter_response"
    responses_url = urljoin(URL, responses_api)

    #Get the response from API
    data_date_range = date_range
    json_data = json.dumps(data_date_range)
    response = requests.post(responses_url, data = json_data, headers = {'User': API_KEY})
    response_data = response.json()
    #Compare the two response recieved with the actual response
    diff = [i for i in response_data + expected_response if i not in response_data or i not in expected_response]
    result = len(diff) == 0
    print(date_range)

    assert response.status_code == 200
    assert len(response_data) == len(expected_response)
    assert result == True,f'There are {len(diff)} differences:\n{diff[:5]}'
