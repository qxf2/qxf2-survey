"""
This module contains the cypher queries required to communicate with the backend
"""

IMPORT_EMPLOYEES = """LOAD CSV WITH HEADERS FROM $path as row\
                      MERGE (e:Employees {fullName: row.fullName,\
                                          ID: toInteger(row.ID),\
                                          firstName: row.firstName,\
                                          lastName: coalesce(row.lastName,""),\
                                          email: row.email,\
                                          status: row.status})"""

IMPORT_EMPLOYEES_HELPTAKEN = """LOAD CSV WITH HEADERS FROM $path as row\
                                WITH row where row.helptaken_dates is not null\
                                MERGE (a:Employees { fullName: row.fullName })\
                                MERGE (b:Employees { fullName: row.helptaken_names })\
                                MERGE (a)<-[x:TAKEN { helptaken: split(substring(replace(replace(row.helptaken_dates,"'","")," ",""), 1, size(replace(replace(row.helptaken_dates,"'","")," ","")) -2),",") }]-(b)"""

IMPORT_EMPLOYEES_HELPGIVEN = """LOAD CSV WITH HEADERS FROM $path as row\
                                WITH row where row.helpgiven_dates is not null\
                                MERGE (a:Employees { fullName: row.fullName })\
                                MERGE (b:Employees { fullName: row.helpgiven_names })\
                                MERGE (a)-[x:GIVEN { helpgiven: split(substring(replace(replace(row.helpgiven_dates,"'","")," ",""), 1, size(replace(replace(row.helpgiven_dates,"'","")," ","")) -2), ",") }]->(b)"""

IMPORT_EMPLOYEES_LEARNT_TECHS = """LOAD CSV WITH HEADERS FROM $path AS row\
                                   WITH row where row.technology_name is not null\
                                   MERGE (e:Employees { fullName: row.fullName })\
                                   MERGE (t:Technology { technology_name: row.technology_name })\
                                   MERGE (e)-[z:KNOWS { learnt_dates: split(substring(replace(replace(row.learnt_dates,"'","")," ",""), 1, size(replace(replace(row.learnt_dates,"'","")," ","")) -2), ",") }]-(t)"""

IMPORT_TECHS = "LOAD CSV WITH HEADERS FROM $path as row\
                MATCH (t:Technology)\
                WHERE t.technology_name = row.technology_name\
                SET t.first_seen = row.first_seen"


GET_USER_NAME = "MATCH (e:Employees)\
                 RETURN e.fullName, e.email"

GET_USER_ID = "MATCH (e:Employees)\
               RETURN e.ID, e.email"

GET_ACTIVE_USER_ID =  "MATCH (e:Employees)\
                       WHERE e.status='Y'\
                       RETURN e.ID"

SET_GIVEN_PROP = "MATCH (a:Employees { fullName: $user_name })-[r:GIVEN]->(b:Employees { fullName: $helped_name })\
                  WHERE NOT $date in r.helpgiven\
                  SET r.helpgiven = coalesce(r.helpgiven, []) + $date"

SET_TAKEN_PROP = "MATCH (a:Employees { fullName: $user_name })<-[r:TAKEN]-(b:Employees { fullName: $helped_name })\
                  WHERE NOT $date in r.helptaken\
                  SET r.helptaken = coalesce(r.helptaken, []) + $date"

CREATE_TAKEN_REL = "MERGE (a:Employees { fullName: $user_name })\
                    MERGE (b:Employees { fullName: $helped_name })\
                    MERGE (a)<-[x:TAKEN]-(b)"


CREATE_GIVEN_REL = "MERGE (a:Employees { fullName: $user_name })\
                    MERGE (b:Employees { fullName: $helped_name })\
                    MERGE (a)-[y:GIVEN]->(b)"

GET_TECHS = "MATCH (t:Technology)\
             RETURN t.technology_name"

SET_TECH_PROP = "MATCH (e:Employees { fullName: $name})-[z:KNOWS]-(t:Technology { technology_name: $tech})\
                 SET t.first_seen = $date_seen"

SET_TECH_REL_PROP = "MATCH (e:Employees { fullName: $name})-[z:KNOWS]-(t:Technology { technology_name: $tech})\
                     WHERE NOT EXISTS(z.learnt_dates) OR NOT $date in z.learnt_dates\
                     SET z.learnt_dates = coalesce(z.learnt_dates, []) + $date"

CREATE_TECH_REL = "MERGE (e:Employees { fullName: $name})\
                   MERGE (t:Technology { technology_name: $tech})\
                   MERGE (e)-[z:KNOWS]-(t)"

DELETE_USER = "MATCH (e:Employees { ID: $id })\
               DETACH DELETE e"

GET_ALL_USERS = "MATCH (e:Employees)\
                 RETURN e ORDER BY e.ID"

GET_USERS_BY_ID = "MATCH (e:Employees { ID: $id }) RETURN e"

CHECK_IF_RESPONDED = ["MATCH (a:Employees)-[x:GIVEN]->(b:Employees) WHERE $date in x.helpgiven return a.ID",
                      "MATCH (a:Employees)<-[y:TAKEN]-(b:Employees) WHERE $date in y.helptaken return a.ID",
                      "MATCH (a:Employees)-[z:KNOWS]-(b:Technology) WHERE $date in z.learnt_dates return a.ID"]

QELO_TECHNOLOGY = "MATCH (m:Employees)-[r]->(n:Technology)\
                   RETURN m.ID AS respondent_id,n.technology_name AS technology,r.learnt_dates AS date"
