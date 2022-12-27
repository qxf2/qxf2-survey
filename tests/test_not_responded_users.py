"""
Tests for survey API endpoint '/survey​/admin​/not_responded_users' 
  that fetches all the users that have not responded to the survey
Test cases:
 * Check the employees that have not responded to the survey and are active
 * Mock response given from an employee and verify that the employee is not listed 
"""

import os
from datetime import datetime
import sys
from urllib.parse import urljoin
import requests
import pytest
from dateutil.relativedelta import relativedelta
from dateutil.relativedelta import FR

sys.path.append(os.path.join(os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), "backend"), "app"))
from db import session as db
from core import config


GRAPH = db.auth()

CREATE_GIVEN_RELATION = "MERGE (a:Employees { fullName: $from })\
                    MERGE (b:Employees { fullName: $to })\
                    MERGE (a)-[y: GIVEN]->(b)"
CREATE_TAKEN_RELATION = "MERGE (a:Employees { fullName: $from })\
                    MERGE (b:Employees { fullName: $to })\
                    MERGE (a)-[y: TAKEN]->(b)"
SET_TAKEN_RELATION_DATE = "MATCH (a:Employees { fullName: $from })-[r:TAKEN]->(b:Employees { fullName: $to})\
                  WHERE NOT EXISTS(r.helptaken)\
                  OR NOT $date in r.helptaken\
                  SET r.helptaken = coalesce(r.helptaken, []) + $date"
SET_GIVEN_RELATION_DATE = "MATCH (a:Employees { fullName: $from })-[r:GIVEN]->(b:Employees { fullName: $to})\
                  WHERE NOT EXISTS(r.helpgiven)\
                  OR NOT $date in r.helpgiven\
                  SET r.helpgiven = coalesce(r.helpgiven, []) + $date"

URL = config.URL
API_KEY = config.API_KEY


# Get the url for the API endpoint that returns list of users who have not responded
RESPONSES_URL = urljoin(URL, "survey/admin/not_responded_users")

TEST_DATA = [
    (  # Case where no employees responded - return all employees who are active
        {}, [{
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
        ]),
    (
        {'from': 'Generous Giver', 'to': 'Generous Taker', 'action': 'GIVEN'},
        [
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
        ]
    )
]


@pytest.mark.parametrize("relation,expected_response", TEST_DATA)
def test_not_responded_users(relation, expected_response):
    "Test the response data received for employees that have not responded or taken the survey"

    add_relation(relation)
    # Get the response from API
    response = requests.get(RESPONSES_URL, headers={'User': API_KEY})
    response_data = response.json()
    # Compare the two response recieved with the actual response
    diff = [i for i in response_data +
            expected_response if i not in response_data or i not in expected_response]
    result = len(diff) == 0
    assert response.status_code == 200
    assert len(response_data) == len(expected_response)
    assert result is True, f'There are {len(diff)} differences:\n{diff}'


def add_relation(relation):
    "Add relation to employees to mock that employees have taken the survey"
    if "action" not in relation:
        return
    date = (datetime.now() + relativedelta(weekday=FR(0))).strftime("%Y-%m-%d")

    frm = relation["from"]
    to = relation["to"]
    action = relation["action"]
    if action == 'GIVEN':
        GRAPH.run(CREATE_GIVEN_RELATION, parameters={"from": frm, "to": to})
        GRAPH.run(SET_GIVEN_RELATION_DATE, parameters={
                  "from": frm, "to": to, "date": date})
    elif action == 'TAKEN':
        GRAPH.run(CREATE_TAKEN_RELATION, parameters={"from": frm, "to": to})
        GRAPH.run(SET_TAKEN_RELATION_DATE, parameters={
                  "from": frm, "to": to, "date": date})
