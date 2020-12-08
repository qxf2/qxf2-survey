"""
This module models the endpoints in the survey app
"""

from fastapi import APIRouter
from .routes import survey, admin

app = APIRouter()

app.include_router(router=survey.router, prefix="", tags=["Response"])
app.include_router(router=admin.router, prefix="/admin", tags=["Admin"])
