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
