"""
This module contains the methods related to the nodes with employee label in the database
"""
import os
import sys
from pandas import DataFrame
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(\
                                                   os.path.abspath(__file__))))))
from db import session
from db.queries import cypher
import pandas as pd
#from flask import jsonify

GRAPH = session.auth()


def get_user_name(email):
    "returns the Full name of a given employee email"
    users = DataFrame(GRAPH.run(cypher.GET_USER_NAME), columns=['fullName', 'email'])
    user_name = users.loc[users['email'] == email, 'fullName'].iloc[0]
    return user_name


def get_user_id(email=None, all_users=False):
    "returns the id of a given employee email"
    users = DataFrame(GRAPH.run(cypher.GET_USER_ID), columns = ['ID', 'email'])
    if all_users:
        return users.ID.values.tolist()
    if email is None:
        user_id = users['ID'].iloc[-1]
    else:
        user_id = users.loc[users['email'] == email, 'ID'].iloc[0]
    return user_id

def get_active_user_id(email=None, all_users=False):
    "returns the id of a given active user employee email"
    active_users=list(GRAPH.run(cypher.GET_ACTIVE_USER_ID))
    users = DataFrame(active_users, columns = ['ID'])
    if all_users:
        return users.ID.values.tolist()
    if email is None:
        user_id = users['ID'].iloc[-1]
    else:
        user_id = users.loc[users['email'] == email, 'ID'].iloc[0]
    return user_id

def set_employee_relation_properties(help_type, name, helped, date):
    "sets the properties of employee relationship based on the given help_type"
    if help_type=="given":
        GRAPH.run(cypher.SET_GIVEN_PROP,\
                  parameters = {"user_name":name, "helped_name":helped, "date":date})
    else:
        GRAPH.run(cypher.SET_TAKEN_PROP,\
                  parameters = {"user_name":name, "helped_name":helped, "date":date})


def create_help_relation(help_type, name, helped, date):
    "creates the relationship between the employee nodes"
    if help_type == "taken":
        GRAPH.run(cypher.CREATE_TAKEN_REL,\
                  parameters={"user_name":name, "helped_name":helped})
    else:
        GRAPH.run(cypher.CREATE_GIVEN_REL,\
                   parameters={"user_name":name, "helped_name":helped})
    set_employee_relation_properties(help_type, name, helped, date)


def get_not_responded_user_emails(responded_users):
    "returns a list of employee emails who are yet to respond to the survey"
    responded_user_ids = [item for sublist in responded_users for item in sublist]
    user_ids = get_active_user_id(all_users=True)
    non_responded_user_ids = list(set(user_ids)-set(responded_user_ids))
    non_responded_users = []
    for user_id in non_responded_user_ids:
        user = list(GRAPH.run(cypher.GET_USERS_BY_ID, parameters={"id": user_id}))
        non_responded_users.append(user[0])
    employee_list = [employee[0] for employee in non_responded_users]
    return employee_list


def get_symmetry_score(start_date, end_date, responses, active_employees):
    "Calculate the symmetry"

    enddate = end_date

    #3/6months from today For 3months set days = 90 , 6 months = 180
    startdate= start_date
    emp_name = pd.DataFrame(active_employees)
    responses = pd.DataFrame(responses)

    error="No data found for this search"
    #who helped you
    print(responses)
    rbd_helped_you=responses[(responses.date >= startdate)&(responses.date <= enddate)&(responses.question_no==1) &(responses.answer.isin(emp_name.name))].groupby(responses.answer).size()
    rbd_helped_you=normalize_scores(rbd_helped_you)
    #whom did you help
    rbd_you_helped=responses[(responses.date >= startdate)&(responses.date <= enddate)&(responses.question_no==2)&(responses.answer.isin(emp_name.name))].groupby(responses.answer).size()
    rbd_you_helped=normalize_scores(rbd_you_helped)
    rbd_symmetry_score={}
    name=[]
    score=[]
    #iterating through the dataframes of helped data and calculated Symmetry score for each employee
    for help_name,help_score in rbd_helped_you.items():
        rbd_symmetry_score[help_name]=help_score*100.0/rbd_you_helped[help_name]
        name.append(help_name)
        score.append(rbd_symmetry_score[help_name])

    employee_name=[employee_name for _,employee_name in sorted(zip(score,name),reverse=True)]
    score.sort(reverse=True)

    if len(employee_name) != 0:
        overall_symmetry_score={"employee_name":  employee_name, "data":score,"error":" "}
    else:
        overall_symmetry_score={"employee_name":  employee_name, "data":score,"error":error}


    return overall_symmetry_score

def normalize_scores(my_dict):
  "Normalize the scores to be between 0 and 1"
  max_score = get_max_score(my_dict)
  for name,score in my_dict.items():
    my_dict[name] = score*100/max_score

  return my_dict

def get_max_score(my_dict):
    "Return the max score in a (name:score) dict"
    max_score = 0
    for key,val in my_dict.items():
        if max_score < val:
            max_score = val

    return max_score

def get_response_rate(startdate,enddate,responses,userid,user_list):
    "Get the overall response rate for the date range"

    responses = pd.DataFrame(responses)
    userid = pd.DataFrame(userid)
    user_list = pd.DataFrame(user_list)

    error="No data found for this search"   
    #responses table date within date range and for active employees
    options=userid['id']
    userlist=user_list
    #survey data in the data range for current active users 
    survey_data_inrange=responses[(responses.date >= startdate)&(responses.date <= enddate) &(responses.respondent_id.isin(options))]
    response_rate={}
    emp_name=[]
    response_data=[]
    #iterating through users and finding their total surveys and if their first survey is before or within selected date range and calculating total surveys for each user
    for index,row in userlist.iterrows():
        surveys_taken=survey_data_inrange[survey_data_inrange.respondent_id==row['id']].groupby(['date']).size().count()
        first_survey_date=survey_data_inrange[survey_data_inrange.respondent_id==row['id']]['date'].min()
        total_surveys=responses[(responses.date >= first_survey_date)&(responses.date <= enddate)].date.nunique() 
        if (surveys_taken !=0 and total_surveys !=0):
            resp_rate=(surveys_taken*100)/total_surveys
            emp_name.append(row['name'])
            response_data.append(resp_rate)
    employee_name=[employee_name for _,employee_name in sorted(zip(response_data,emp_name),reverse=True)]
    response_data.sort(reverse=True)    
    if len(employee_name) != 0 :
        overall_response_rate={"name":employee_name,"response_data":response_data,"error":" "}
    else:   
        overall_response_rate={ "name":employee_name,"response_data":response_data,"error":error}

    return overall_response_rate

