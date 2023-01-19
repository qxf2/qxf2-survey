"""
Test for survey API endpoint `/survey/response` that is used to submit the survey response.
The response is stored on the Friday of the current week.
Test cases that will be covered in this test:
1) Test Case 1
    - Submit a response with help data and technology learnt data
    - Use /survey/admin/QElo_filter_response & /survey/admin/QElo_filter_technology
    endpoints to validate the data stored
2) Test Case 2:
    - Submit two unique responses with the same user
    - Validate both the responses are stored using /survey/admin/QElo_filter_response
    & /survey/admin/QElo_filter_technology endpoints
3) Test Case 3:
    - Submit two similar responses with the same user. Make sure the help data
    and technology learnt data are the same in both responses submitted
    - Validate if the responses submitted are stored only once and not duplicated.
"""
import json
from urllib.parse import urljoin
from datetime import datetime, timedelta
import requests
import pytest
from decouple import config

URL = config("URL")
API_KEY = config("API_KEY")

# Get the url to submit survey response
SUBMIT_SURVEY_URL = urljoin(URL, "survey/response")

# Get the url for the API endpoint that fetches user responses b/w two given dates
RESPONSES_URL = urljoin(URL, "survey/admin/QElo_filter_response")

# Get the url for the API endpoint that fetches technologies learnt b/w two given dates
TECHNOLOGY_URL = urljoin(URL, "survey/admin/QElo_filter_technology")

# Get date range of current week ie: Monday to Friday
CURRENT_WEEK_DATE_RANGE = {
    "start_date": (datetime.now() - timedelta(days=datetime.now().weekday())).strftime(
        "%Y-%m-%d"
    ),
    "end_date": (
        datetime.now() + timedelta(days=(4 - datetime.now().weekday()))
    ).strftime("%Y-%m-%d"),
}

TEST_DATA = [
    # Submit valid response
    (
        {
            "userMail": "generoustaker@qxf2.com",
            "listHelp": [
                {"label": "Generous Giver", "value": "generousgiver@qxf2.com"}
            ],
            "listHelped": [
                {"label": "Generous Giver", "value": "generousgiver@qxf2.com"}
            ],
            "listTags": "__TEST__PYTHON",
        },
        #Expected help response data for the valid response submitted
        [
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 1,
                "answer": "Generous Giver",
            },
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 2,
                "answer": "Generous Giver",
            },
        ],
        #Expected technology data for the valid response submitted
        [
            {
                "respondent_id": 2,
                "technology": "__TEST__PYTHON",
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
            }
        ],
    ),
    #Submit another unique response
    (
        {
            "userMail": "generoustaker@qxf2.com",
            "listHelp": [{"label": "Smart Learner", "value": "smart_learner@qxf2.com"}],
            "listHelped": [
                {"label": "Smart Learner", "value": "smart_learner@qxf2.com"}
            ],
            "listTags": "__TEST__RUST",
        },
        #Check if newly submitted unique response data is appended to the previous help response data
        [
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 1,
                "answer": "Generous Giver",
            },
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 2,
                "answer": "Generous Giver",
            },
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 1,
                "answer": "Smart Learner",
            },
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 2,
                "answer": "Smart Learner",
            },
        ],
        #Check if newly submitted unique response data is appended to the previous technology response data
        [
            {
                "respondent_id": 2,
                "technology": "__TEST__PYTHON",
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
            },
            {
                "respondent_id": 2,
                "technology": "__TEST__RUST",
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
            },
        ],
    ),
    # Submit the same response again
    (
        {
            "userMail": "generoustaker@qxf2.com",
            "listHelp": [{"label": "Smart Learner", "value": "smart_learner@qxf2.com"}],
            "listHelped": [
                {"label": "Smart Learner", "value": "smart_learner@qxf2.com"}
            ],
            "listTags": "__TEST__RUST",
        },
        # The help response data should remain the same and should not have duplicate entries
        [
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 1,
                "answer": "Generous Giver",
            },
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 2,
                "answer": "Generous Giver",
            },
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 1,
                "answer": "Smart Learner",
            },
            {
                "respondent_id": 2,
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
                "question_no": 2,
                "answer": "Smart Learner",
            },
        ],
        # The technology response data should remain the same and should not have duplicate values
        [
            {
                "respondent_id": 2,
                "technology": "__TEST__PYTHON",
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
            },
            {
                "respondent_id": 2,
                "technology": "__TEST__RUST",
                "date": CURRENT_WEEK_DATE_RANGE["end_date"],
            },
        ],
    ),
]


@pytest.mark.parametrize(
    "submit_response_data, expected_help_response, expected_tech_response", TEST_DATA
)
def test_post_survey_response(
    submit_response_data, expected_help_response, expected_tech_response
):
    "Used to submit survey response and validate result"
    # Submit survey response
    submit_response = requests.post(
        SUBMIT_SURVEY_URL,
        data=json.dumps({"data": submit_response_data}),
        headers={"User": API_KEY},
        timeout=5,
    )
    submit_response_msg = submit_response.json()

    # Get difference between expected response and actual response for help data
    help_response_data = get_help_response()
    help_response_diff = compare_responses(help_response_data, expected_help_response)
    help_response_result = len(help_response_diff) == 0

    # Get difference between expected response and actual response for technology_data
    tech_response_data = get_tech_response()
    tech_response_diff = compare_responses(tech_response_data, expected_tech_response)
    tech_response_result = len(tech_response_diff) == 0

    assert submit_response_msg == {"msg": "Successfully recorded survey response"}
    assert len(help_response_data) == len(expected_help_response)
    assert (
        help_response_result is True
    ), f"There are {len(help_response_diff)} differences:\n{help_response_diff}"
    assert len(tech_response_data) == len(expected_tech_response)
    assert (
        tech_response_result is True
    ), f"There are {len(tech_response_diff)} differences:\n{tech_response_diff}"


def get_help_response():
    "Used to get the help reponses b/w two given dates"

    response = requests.post(
        RESPONSES_URL,
        data=json.dumps(CURRENT_WEEK_DATE_RANGE),
        headers={"User": API_KEY},
        timeout=5,
    )
    response_data = response.json()
    return response_data


def get_tech_response():
    "Used to get technologies learnt b/w two given dates"

    tech_response = requests.post(
        TECHNOLOGY_URL,
        data=json.dumps(CURRENT_WEEK_DATE_RANGE),
        headers={"User": API_KEY},
        timeout=5,
    )
    tech_data = tech_response.json()
    return tech_data


def compare_responses(response_data, expected_response):
    "Used to compare the expected response with the actual response"
    response_diff = [
        i
        for i in response_data + expected_response
        if i not in response_data or i not in expected_response
    ]
    return response_diff
