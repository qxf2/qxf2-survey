"""
This module models the api request bodies
"""

from typing import Dict
from pydantic import BaseModel
import datetime

class EmployeeData(BaseModel):
    "request body"
    data: Dict


class EmployeeRegistration(BaseModel):
    "request body"
    data: Dict

class FetchTechnology(BaseModel):
    "request body"
    date: datetime.date

class FetchResponses(BaseModel):
    "request body"
    start_date: datetime.date
    end_date: datetime.date

class EmployeeEmail(BaseModel):
    "request body"
    email: str
