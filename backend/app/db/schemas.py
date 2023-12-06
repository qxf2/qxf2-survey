"""
This module models the api request bodies
"""

from typing import Dict
from pydantic import BaseModel, Field
import datetime

class EmployeeData(BaseModel):
    "request body"
    data: Dict


class EmployeeRegistration(BaseModel):
    "request body"
    data: Dict

class FetchTechnology(BaseModel):
    "request body"
    date:str = Field(example="1980-01-25")

class FetchResponses(BaseModel):
    "request body"
    start_date: str = Field(example="1970-01-01")
    end_date: str = Field(example="2023-01-01")

class EmployeeEmail(BaseModel):
    "request body"
    email: str

class EmployeeStatus(BaseModel):
    "request body"
    employee_status: str
