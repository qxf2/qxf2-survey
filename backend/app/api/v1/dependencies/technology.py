"""
This module contains the methods related to the nodes with technology label in the database
"""

from pandas import DataFrame
from db.queries import cypher
from db import session

GRAPH = session.auth()


def is_new(tech):
    "checks if the given technology is a new entry in the database"
    techs = DataFrame(GRAPH.run(cypher.GET_TECHS), columns=['Technology'])
    tech_list = techs.Technology.values.tolist()
    flag = True
    if tech.upper() in tech_list:
        flag = False
    return flag


def set_new_technology_properties(name, tech, date):
    "sets the properties of a new technology node in the database"
    GRAPH.run(cypher.SET_TECH_PROP,\
              parameters={"name":name, "tech":tech.upper(), "date_seen":date})


def set_technology_relationship_properties(name, tech, date):
    "sets the property of relationship between an employee and a technology, if there isn't one"
    GRAPH.run(cypher.SET_TECH_REL_PROP,\
              parameters={"name":name, "tech":tech.upper(), "date":date})


def create_tech_relation(name, tech, date):
    "creates the relationship between an employee and a technology"
    flag = is_new(tech)
    GRAPH.run(cypher.CREATE_TECH_REL,\
              parameters={"name":name, "tech":tech.upper()})
    if flag:
        set_new_technology_properties(name, tech, date)
    set_technology_relationship_properties(name, tech, date)
