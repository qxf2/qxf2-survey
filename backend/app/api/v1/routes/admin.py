"""
This module contains the endpoints related to Admin page in the frontend
"""

import os
import sys
from datetime import datetime , timedelta, date
from dateutil.relativedelta import relativedelta, FR
from fastapi import APIRouter, Depends, Form, HTTPException
from py2neo import Node
from ..dependencies.employee import get_user_id, get_not_responded_user_emails
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(\
                                                   os.path.abspath(__file__))))))
from core import security
from db.queries import cypher
from db import schemas, session as db
from google.oauth2 import id_token
from google.auth.transport import requests
from decouple import config
import secrets
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
import json
from db.queries import graphql_queries 
import requests as req

router = APIRouter()
GRAPH = db.auth()

BASE_URL = 'https://qxf2-employees.qxf2.com/graphql'

def authenticate():
    "Return an authenticate code"
    auth_query = graphql_queries.authorise

    response = req.post(url = BASE_URL, json = {'query': auth_query})

    return response.json().get('data',{}).get('auth',{}).get('accessToken',None)

@router.get('/employees')
def get_employee_data(authenticated: bool = Depends(security.validate_request)):
    "returns the employee details"

    fetch_employees = graphql_queries.fetch_employees
    access_token = authenticate()
    headers = {'Authorization': f'Bearer {access_token}'}
    response = req.get(url = BASE_URL, json = {'query': fetch_employees}, headers =\
        headers)
    all_employees = response.json().get('data', {}).get('allEmployees', {}).get('edges', [])
    employee_list=[]
    for employee in all_employees:
        fullname = employee['node']['firstName'] + " " + employee['node']['lastName']
        employee['node']['fullName'] = fullname
        employee_list.append(employee['node'])
    
    return employee_list

@router.post('/new_employee')
def get_new_employee_data(user: schemas.EmployeeRegistration,\
                          authenticated: bool = Depends(security.validate_request)):
    "creates the new user node in the neo4j upon new employee registration"
    emp_data = user.data
    last_user_id = get_user_id(email=None)
    print("Test message")
    print(last_user_id)
    new_employee = Node("Employees",
                         ID=int(last_user_id)+1,
                         firstName=emp_data["firstName"],
                         lastName=emp_data["lastName"],
                         email=emp_data["email"],
                         fullName=emp_data["fullName"],
                         status=emp_data["status"])
    try:
        GRAPH.create(new_employee)
        return {"msg": "Successfully registered new employee"}
    except:
        return {"msg": "New employee registration failed"}


@router.delete('/employees/{id}')
def delete_employee(id: int,  authenticated: bool = Depends(security.validate_request)):
    "delete the user with a given id as a query parameter"
    try:
        GRAPH.run(cypher.DELETE_USER, parameters={"id": id})
        return {"msg": f"Successfully deleted employee with id {id}"}
    except:
        return {"msg": f"Unable to delete employee with id {id}"}

@router.post('/get_employee_by_email')
def get_employee_by_email(email: schemas.EmployeeEmail, 
                          authenticated: bool = Depends(security.validate_request)):
    "Return employee details by email"
    employee_email = email.email
    employee_details = GRAPH.run(cypher.GET_USER_BY_EMAIL,
                             parameters={"email":str(employee_email)}).data()
    if not employee_details:
        return "Employee does not exist"
    else:
        return employee_details

@router.post('/update_employee_status')
def set_employee_status(email: schemas.EmployeeEmail, status: schemas.EmployeeStatus,
                          authenticated: bool = Depends(security.validate_request)):
    "Return employee details by email"
    employee_email = email.email
    employee_status = status.employee_status
    if employee_status.upper() == "Y" or employee_status.upper() == "N":
        try:
            update_employee_status = GRAPH.run(cypher.SET_USER_STATUS,
                                    parameters={"email":str(employee_email),"status":str(employee_status)}).data()
            return{f"Successfully updated status of employee with email {employee_email}"}
        except:
            return{f"Unable to set status of employee with email {employee_email}"}
    else:
        return "Please enter either Y or N as status"

@router.get('/not_responded_users')
def get_employees_yet_to_respond(authenticated: bool = Depends(security.validate_request)):
    "returns a list of employee who are yet to respond to the survey"
    today = datetime.now().strftime("%Y-%m-%d")
    friday = (datetime.now() + relativedelta(weekday=FR(0))).strftime("%Y-%m-%d")
    responded_users = []
    #if today == friday:
    for check in cypher.CHECK_IF_RESPONDED:
        try:
            user_id = (GRAPH.run(check,parameters={"date": friday})).to_data_frame()
            user_id = list(set((user_id['a.ID'])))
            responded_users.append(user_id)
        except:
            print("Trying to check if the user has responded today")
    employee_list = get_not_responded_user_emails(responded_users)
    return employee_list

@router.get('/QElo_users')
def qelo_get_users(authenticated: bool = Depends(security.validate_request)):
    "Simulates the user node of quilt for QElo score computation"
    qelo_users = GRAPH.run(cypher.QELO_USERS).data()
    return qelo_users

@router.get('/QElo_technology')
def qelo_get_technology(authenticated: bool = Depends(security.validate_request)):
    "returns the technologies with coloumns that is mapped for QElo score computation"
    qelo_technology = GRAPH.run(cypher.QELO_TECHNOLOGY).data()
    return qelo_technology


@router.get('/QElo_response')
def qelo_get_response(authenticated: bool = Depends(security.validate_request)):
    "simulates the response node of quilt for QElo score computation"
    qelo_response = GRAPH.run(cypher.QELO_RESPONSE).data()
    return qelo_response

@router.post('/techs_learnt_on_week')
def technologies_learnt_on_week(fetched_date: schemas.FetchTechnology,
                                authenticated: bool = Depends(security.validate_request)):
    "returns all the technologies learnt in the week for a given date"
    date = fetched_date.date
    monday = date - timedelta(days=date.weekday())
    friday = (date + relativedelta(weekday=FR(0))).strftime("%Y-%m-%d")
    technologies = GRAPH.run(cypher.TECHNOLOGIES_LEARNT_ON_PARTICULAR_WEEK,
                             parameters={"date_monday":str(monday),
                             "date_friday":str(friday)}).data()
    return technologies

@router.post('/QElo_filter_response')
def qelo_get_response_between_given_dates(fetched_date: schemas.FetchResponses,
                                          authenticated: bool = Depends(security.validate_request)):
    "simulates the response node of quilt for QElo score computation"

    start_date = fetched_date.start_date
    end_date = fetched_date.end_date
    qelo_response = GRAPH.run(cypher.QELO_RESPONSE_BETWEEN_DATES,
                              parameters={"start_date":str(start_date),
                              "end_date":str(end_date)}).data()
    return qelo_response

@router.post('/QElo_filter_technology')
def qelo_get_technology_between_given_dates(fetched_date: schemas.FetchResponses,
                                            authenticated: bool = Depends(security.validate_request)):
    "simulates the technology node of quilt for QElo score computation"

    start_date = fetched_date.start_date
    end_date = fetched_date.end_date
    qelo_technology = GRAPH.run(cypher.QELO_TECHNOLOGY_BETWEEN_DATES,
                                parameters={"start_date":str(start_date),
                                "end_date":str(end_date)}).data()
    return qelo_technology

@router.post('/admin-login')
def admin_login(idtoken: str = Form(...),
                authenticated: bool = Depends(security.validate_request)):
    "handle admin login"

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        CLIENT_ID = config("CLIENT_ID")
        idinfo = id_token.verify_oauth2_token(idtoken, requests.Request(), CLIENT_ID)
        emails = json.loads(config("ADMIN_EMAIL"))
        email_match = False
        for email in emails:
            # ID token is valid. Get the user's Google Account ID from the decoded token.
            if secrets.compare_digest(idinfo['email'], str(email)):
                email_match = True
                break
        if email_match == False:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED, detail="User Unauthorized", headers={}
            )
        return True
    except ValueError:
        # Invalid token
        return ValueError




