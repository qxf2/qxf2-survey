"""
This module models the api request bodies
"""

from typing import Dict
from pydantic import BaseModel

class EmployeeData(BaseModel):
    "request body"
    data: Dict


class EmployeeRegistration(BaseModel):
    "request body"
    data: Dict
    