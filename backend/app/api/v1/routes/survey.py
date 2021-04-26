"""
This module contains the endpoints related to Survey page in the frontend
"""

import os
import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta, FR
from fastapi import APIRouter
from ..dependencies.employee import get_user_name, create_help_relation
from ..dependencies.technology import create_tech_relation
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(\
                                                   os.path.abspath(__file__))))))
from db import schemas

router = APIRouter()


@router.post('/response')
def get_survey_response(response: schemas.EmployeeData):
    "creates the required nodes in the neo4j upon submitting the survey"
    survey_response = response.data
    user = get_user_name(survey_response.get("userMail"))
    date = (datetime.now() + relativedelta(weekday=FR(0))).strftime("%Y-%m-%d")
    try:
        for name in survey_response.get("listHelp"):
            helptaken_name = name.get('label')
            create_help_relation("taken", user, helptaken_name, date)
        for name in survey_response.get("listHelped"):
            helpgiven_name = name.get('label')
            create_help_relation("given", user, helpgiven_name, date)
        for tech in survey_response.get("listTags").split(","):
            create_tech_relation(user, tech, date)
        return {"msg": "Successfully recorded survey response"}
    except Exception as error:
        return {"msg": f"Failed to record survey response: {error}"}
