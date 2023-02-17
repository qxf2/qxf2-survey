"""
This module contains the cypher queries required to communicate with the backend
"""

IMPORT_EMPLOYEES = """LOAD CSV WITH HEADERS FROM $path as row\
                      MERGE (e:Employees {fullName: row.fullName,\
                                          ID: toInteger(row.ID),\
                                          firstName: row.firstName,\
                                          lastName: coalesce(row.lastName,""),\
                                          email: row.email,\
                                          author_name: coalesce(row.author_name,""),\
                                          status: row.status})"""

IMPORT_EMPLOYEES_HELPTAKEN = """LOAD CSV WITH HEADERS FROM $path as row\
                                WITH row where row.helptaken_dates is not null\
                                MERGE (a:Employees { fullName: row.fullName })\
                                MERGE (b:Employees { fullName: row.helptaken_names })\
                                MERGE (a)-[x:TAKEN { helptaken: split(substring(replace(replace(row.helptaken_dates,"'","")," ",""), 1, size(replace(replace(row.helptaken_dates,"'","")," ","")) -2),",") }]->(b)"""

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
                MERGE (t:Technology {technology_name: row.technology_name,\
                first_seen: row.first_seen})"

GET_USER_NAME = "MATCH (e:Employees)\
                 RETURN e.fullName, e.email"

GET_USER_ID = "MATCH (e:Employees)\
               RETURN e.ID, e.email\
               ORDER BY e.ID ASC"

GET_ACTIVE_USER_ID = "MATCH (e:Employees)\
                      WHERE e.status='Y'\
                      RETURN e.ID"

GET_USER_BY_EMAIL = "MATCH (e:Employees)\
                     WHERE e.email=$email\
                     RETURN e AS employee_details"

SET_USER_STATUS = "MATCH (e:Employees)\
                   WHERE e.email=$email\
                   SET e.status=$status"

GET_ACTIVE_USER_NAME = "MATCH (e:Employees)\
                        WHERE e.status='Y'\
                        AND NOT e.firstName IN ['','External','Edward','Shrihari','Kavitha']\
                        RETURN e.fullName as name"

GET_ACTIVE_USER_LIST = "MATCH (e:Employees)\
                        WHERE e.status='Y'\
                        AND NOT e.firstName IN ['','External','Edward','Shrihari','Kavitha']\
                        RETURN e.fullName as name, e.ID as id"

GET_ACTIVE_USER_IDS = "MATCH (e:Employees)\
                       WHERE e.status='Y'\
                       AND NOT e.firstName IN ['','External','Edward','Shrihari','Kavitha']\
                       RETURN e.ID as id"

SET_GIVEN_PROP = "MATCH (a:Employees { fullName: $user_name })-[r:GIVEN]->(b:Employees { fullName: $helped_name })\
                  WHERE NOT EXISTS(r.helpgiven)\
                  OR NOT $date in r.helpgiven\
                  SET r.helpgiven = coalesce(r.helpgiven, []) + $date"

SET_TAKEN_PROP = "MATCH (a:Employees { fullName: $user_name })-[r:TAKEN]->(b:Employees { fullName: $helped_name })\
                  WHERE NOT EXISTS(r.helptaken)\
                  OR NOT $date in r.helptaken\
                  SET r.helptaken = coalesce(r.helptaken, []) + $date"

CREATE_TAKEN_REL = "MERGE (a:Employees { fullName: $user_name })\
                    MERGE (b:Employees { fullName: $helped_name })\
                    MERGE (a)-[x:TAKEN]->(b)"


CREATE_GIVEN_REL = "MERGE (a:Employees { fullName: $user_name })\
                    MERGE (b:Employees { fullName: $helped_name })\
                    MERGE (a)-[y:GIVEN]->(b)"

GET_TECHS = "MATCH (t:Technology)\
             RETURN t.technology_name"

SET_TECH_PROP = "MATCH (e:Employees { fullName: $name})-[z:KNOWS]-(t:Technology { technology_name: $tech})\
                 SET t.first_seen = $date_seen"

SET_TECH_REL_PROP = "MATCH (e:Employees { fullName: $name})-[z:KNOWS]-(t:Technology { technology_name: $tech})\
                     WHERE NOT EXISTS(z.learnt_dates)\
                     OR NOT $date in z.learnt_dates\
                     SET z.learnt_dates = coalesce(z.learnt_dates, []) + $date"

CREATE_TECH_REL = "MERGE (e:Employees { fullName: $name})\
                   MERGE (t:Technology { technology_name: $tech})\
                   MERGE (e)-[z:KNOWS]-(t)"

DELETE_USER = "MATCH (e:Employees { ID: $id })\
               DETACH DELETE e"

GET_ALL_USERS = "MATCH (e:Employees)\
                 RETURN e ORDER BY e.ID"

GET_USERS_BY_ID = "MATCH (e:Employees { ID: $id })\
                   RETURN e"

CHECK_IF_RESPONDED = [
    "MATCH (a:Employees)-[x:GIVEN]->(b:Employees) WHERE $date in x.helpgiven return a.ID",
    "MATCH (a:Employees)-[y:TAKEN]->(b:Employees) WHERE $date in y.helptaken return a.ID",
    "MATCH (a:Employees)-[z:KNOWS]-(b:Technology) WHERE $date in z.learnt_dates return a.ID",
]

TECHNOLOGIES_LEARNT_ON_PARTICULAR_WEEK = "MATCH (a:Employees)-[z:KNOWS]-(b:Technology)\
                                          WHERE $date_monday in z.learnt_dates\
                                          OR $date_friday in z.learnt_dates\
                                          WITH DISTINCT[a.fullName,b.technology_name] AS output\
                                          RETURN output[0] AS Name,output[1] AS Technology"

QELO_TECHNOLOGY = "MATCH (m:Employees)-[r]->(n:Technology)\
                   RETURN m.ID AS respondent_id,n.technology_name AS technology,r.learnt_dates AS date"

QELO_USERS = "MATCH (e:Employees)\
              RETURN e.ID as id, e.firstName as first_name, e.lastName as last_name,\
              e.email as  email, e.author_name as author_name, e.status as active_flag"

QELO_RESPONSE = "MATCH (m:Employees)-[r]->(n:Employees)\
                 RETURN m.ID AS respondent_id,\
                 CASE type(r)\
                    WHEN 'TAKEN' THEN r.helptaken\
                    WHEN 'GIVEN' THEN r.helpgiven\
                 END AS date,\
                 CASE type(r)\
                    WHEN 'TAKEN' THEN 1\
                    WHEN 'GIVEN' THEN 2\
                 END AS question_no,\
                 n.fullName as answer"

#Query to get responses between two given dates
QELO_RESPONSE_BETWEEN_DATES =  "MATCH (m:Employees)-[r]->(n:Employees)\
                                UNWIND [r.helpgiven,r.helptaken] AS list_helpdates\
                                UNWIND list_helpdates AS helpdate\
                                WITH DISTINCT(helpdate)\
                                WHERE date(helpdate)>=date($start_date)\
                                AND date(helpdate)<=date($end_date)\
                                MATCH (m:Employees)-[r]->(n:Employees)\
                                WHERE helpdate IN r.helpgiven\
                                OR helpdate IN r.helptaken\
                                WITH DISTINCT[m.ID,helpdate,\
                                CASE type(r)\
                                    WHEN 'TAKEN' THEN 1\
                                    WHEN 'GIVEN' THEN 2\
                                END,\
                                n.fullName] AS output\
                                RETURN output[0] AS respondent_id, output[1] AS date,\
                                output[2] AS question_no, output[3] AS answer"

#Query to get  technologies learnt between two given dates
QELO_TECHNOLOGY_BETWEEN_DATES =    "MATCH (m:Employees)-[r]->(n:Technology)\
                                    UNWIND r.learnt_dates AS learnt_date\
                                    WITH DISTINCT(learnt_date)\
                                    WHERE date(learnt_date)>=date($start_date)\
                                    AND date(learnt_date)<=date($end_date)\
                                    MATCH (m:Employees)-[r]->(n:Technology)\
                                    WHERE learnt_date IN r.learnt_dates\
                                    WITH DISTINCT[m.ID,n.technology_name,learnt_date] AS output\
                                    RETURN output[0] AS respondent_id,\
                                    output[1] AS technology,output[2] AS date"

#Delete all the records in the Database(WARNING: Never use this query in production database)
DELETE_ALL_RECORDS = "MATCH (n)\
                      DETACH DELETE n"
