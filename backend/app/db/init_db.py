"""
This module populates the neo4j database with quilt data
"""

import session as db
from queries import cypher

GRAPH = db.auth()

PATH = "file:///"


def import_employee_csvs():
    "imports the csv files related to employee nodes"
    GRAPH.run(cypher.IMPORT_EMPLOYEES,\
              parameters={"path": PATH + "employee.csv"})
    GRAPH.run(cypher.IMPORT_EMPLOYEES_HELPTAKEN,\
              parameters={"path": PATH + "employee_helptaken.csv"})
    GRAPH.run(cypher.IMPORT_EMPLOYEES_HELPGIVEN,\
              parameters={"path": PATH + "employee_helpgiven.csv"})


def import_tech_csvs():
    "imports the csv files related to technology nodes"
    GRAPH.run(cypher.IMPORT_TECHS,\
              parameters={"path": PATH + "technology.csv"})
    GRAPH.run(cypher.IMPORT_EMPLOYEES_LEARNT_TECHS,\
              parameters={"path": PATH + "technology_relationship.csv"})


def init_db():
    "initiate the db with csv imports"
    import_employee_csvs()
    import_tech_csvs()


if __name__ == "__main__":
    init_db()
