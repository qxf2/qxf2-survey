"""
This module contains the cypher queries required to communicate with the backend
"""

IMPORT_EMPLOYEES = """LOAD CSV WITH HEADERS FROM $path as row\
                      MERGE (e:Employees {FullName: row.FullName,\
                                          ID: toInteger(row.ID),\
                                          firstName: row.firstName,\
                                          lastName: coalesce(row.lastName,""),\
                                          email: row.email,\
                                          status: row.status})"""

IMPORT_EMPLOYEES_HELPTAKEN = """LOAD CSV WITH HEADERS FROM $path as row\
                                WITH row where row.helptaken_dates is not null\
                                MERGE (a:Employees { FullName: row.FullName })\
                                MERGE (b:Employees { FullName: row.helptaken_names })\
                                MERGE (a)<-[x:TAKEN { helptaken: split(substring(replace(replace(row.helptaken_dates,"'","")," ",""), 1, size(replace(replace(row.helptaken_dates,"'","")," ","")) -2),",") }]-(b)"""

IMPORT_EMPLOYEES_HELPGIVEN = """LOAD CSV WITH HEADERS FROM $path as row\
                                WITH row where row.helpgiven_dates is not null\
                                MERGE (a:Employees { FullName: row.FullName })\
                                MERGE (b:Employees { FullName: row.helpgiven_names })\
                                MERGE (a)-[x:GIVEN { helpgiven: split(substring(replace(replace(row.helpgiven_dates,"'","")," ",""), 1, size(replace(replace(row.helpgiven_dates,"'","")," ","")) -2), ",") }]->(b)"""

IMPORT_EMPLOYEES_LEARNT_TECHS = """LOAD CSV WITH HEADERS FROM $path AS row\
                                   WITH row where row.technology_name is not null\
                                   MERGE (e:Employees { FullName: row.FullName })\
                                   MERGE (t:Technology { technology_name: row.technology_name })\
                                   MERGE (e)-[z:KNOWS { learnt_dates: split(substring(replace(replace(row.learnt_dates,"'","")," ",""), 1, size(replace(replace(row.learnt_dates,"'","")," ","")) -2), ",") }]-(t)"""

IMPORT_TECHS = "LOAD CSV WITH HEADERS FROM $path as row\
                MATCH (t:Technology)\
                WHERE t.technology_name = row.technology_name\
                SET t.first_seen = row.first_seen"
