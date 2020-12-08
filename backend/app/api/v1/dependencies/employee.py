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
    user_ids = get_user_id(all_users=True)
    non_responded_user_ids = list(set(user_ids)-set(responded_user_ids))
    non_responded_users = []
    for user_id in non_responded_user_ids:
        user = list(GRAPH.run(cypher.GET_USERS_BY_ID, parameters={"id": user_id}))
        non_responded_users.append(user[0])
    employee_list = [employee[0] for employee in non_responded_users]
    return employee_list
