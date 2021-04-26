'''
Test to compare the database after migration
'''
import quilt
import pandas as pd
from backend.app.db import schemas, session as db
from backend.app.db.queries import cypher

GRAPH = db.auth()
app = quilt.load('qxf2/dev_survey')

employee_data=list(GRAPH.run(cypher.GET_ALL_USERS))
employee_list = [employee[0] for employee in employee_data]

def compare_emails():
    "Compares the emails between quilt and neo4j database after migration"
    users = app.users()
    quilt_email=users['email'].values.tolist()
    print("The Employee emails from quilt:",quilt_email)
    neo4j_email=[]
    for employee in employee_list:
        neo4j_email.append(employee['email'])
    print("\nThe Employee emails from Neo4j:",neo4j_email)
    if quilt_email==neo4j_email:
        email_status="\nEmails matches"
    else:
        email_status="\nEmails does not match"

    return email_status

def compare_names():
    "Compares the first name and last name between quilt and neo4j database after migration"
    users = app.users()

    quilt_firstname = users['first_name'].values.tolist()
    quilt_lastname = users['last_name'].values.tolist()
    print("\nThe Employee first names from quilt:",quilt_firstname)
    print("\nThe Employee last names from quilt:", quilt_lastname)

    neo4j_firstname=[]
    for employee in employee_list:
        neo4j_firstname.append(employee['firstName'])

    neo4j_lastname=[]
    for employee in employee_list:
        neo4j_lastname.append(employee['lastName'])

    print("\nThe Employee first names from Neo4j:",neo4j_firstname)
    print("\nThe Employee last names from Neo4j:", neo4j_lastname)

    """
    for quilt,neo in zip(quilt_lastname,neo4j_lastname):
        if quilt==neo:
            print("Name Matching")
        else:
            print("Name not matching")
            print(quilt)
            print(neo)
    """

    if quilt_firstname==neo4j_firstname:
        firstname_status="First names matches"
    else:
        firstname_status="First names does not match"

    if quilt_lastname==neo4j_lastname:
        lastname_status="Last names matches"
    else:
        lastname_status="Last names does not match"

    return firstname_status,lastname_status

def compare_technologies():
    "compares the technologies after migration"
    quilt_technology = app.technology()
    quilt_technology = quilt_technology.drop(['date', 'respondent_id'], axis=1)
    quilt_technology.replace([""], float("NaN"), inplace=True)
    quilt_technology.dropna(inplace=True)
    quilt_technology['technology'] = quilt_technology['technology'].apply(lambda x: x.strip())
    quilt_technology['technology'] = quilt_technology['technology'].str.upper()
    quilt_technology = quilt_technology.drop_duplicates()
    quilt_technology = quilt_technology.sort_values(by='technology')
    quilt_technology = quilt_technology.values.tolist()
    quilt_tech=[]
    for technology in quilt_technology:
        for tech in technology:
            quilt_tech.append(tech)
    print("\nTechnolies before migration:",quilt_tech)
    neo4j_technology = list(GRAPH.run("MATCH (n:Technology) RETURN n.technology_name"))
    neo4j_technology = [tech[0] for tech in neo4j_technology]
    neo4j_technology = sorted(neo4j_technology)
    print("\nTechnolies after migration:",neo4j_technology)

    if quilt_tech == neo4j_technology:
        technology_status = "\nTechnologies matches"
    else:
        technology_status = "\nTechnologies does not match"

    return technology_status





if __name__=="__main__":
    print(compare_emails())
    print(compare_names())
    print(compare_technologies())
