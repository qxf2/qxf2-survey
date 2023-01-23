"""
Tests for survey API endpoint '/survey​/admin​/not_responded_users' 
  that fetches all the users that have not responded to the survey
Test cases:
 * Check the employees that have not responded to the survey and are active
 * Mock response given from an employee and verify that the employee is not listed 
"""

import requests
import pytest
from datetime import date
from urllib.parse import urljoin
from decouple import config

URL = config("URL")
API_KEY = config("API_KEY")

# Get the url for the API endpoint that returns list of users who have not responded
RESPONSES_URL = urljoin(URL, "survey/admin/not_responded_users")

TEST_DATA = [([
  {
    "author_name": "Generous Giver",
    "firstName": "Generous",
    "lastName": "Giver",
    "fullName": "Generous Giver",
    "ID": 1,
    "email": "generousgiver@qxf2.com",
    "status": "Y"
  },
  {
    "author_name": "Generous Taker",
    "firstName": "Generous",
    "lastName": "Taker",
    "fullName": "Generous Taker",
    "ID": 2,
    "email": "generoustaker@qxf2.com",
    "status": "Y"
  },
  {
    "lastName": "Learner",
    "firstName": "Smart",
    "fullName": "Smart Learner",
    "ID": 4,
    "email": "smart_learner@qxf2.com",
    "status": "Y"
  },
  {
    "lastName": "Learner",
    "firstName": "Slow",
    "fullName": "Slow Learner",
    "ID": 5,
    "email": "slow_learner@qxf2.com",
    "status": "Y"
  },
  {
    "lastName": "find me",
    "firstName": "Use my email",
    "fullName": "Use my email to find me",
    "ID": 6,
    "email": "use_this_email_to_find_me@qxf2.com",
    "status": "Y"
  }
])]


@pytest.mark.parametrize("expected_response", TEST_DATA)
def test_not_responded_users(expected_response):
    "Test the response data received for employees that have not responded or taken the survey"
    # Get the response from API
    response = requests.get(RESPONSES_URL, headers={'User': API_KEY})
    response_data = response.json()
    assert response_data == expected_response
