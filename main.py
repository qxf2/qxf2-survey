"""
FastAPI Endpoints for a Sample Message, Database Authentication,
and adding new Nodes to the Database. 
"""

import json
import uvicorn
from fastapi import FastAPI
from py2neo import Node, Graph
from decouple import config

# Grabbing environment variables
HOSTNAME = config("DATABASE_HOST")
USERNAME = config("DATABASE_USERNAME")
PASSWORD = config("DATABASE_PASSWORD")

# Authenticating with the Database
try:
    GRAPH = Graph(HOSTNAME, auth=(USERNAME, PASSWORD))
    DB_FLAG = 0
    # Deleting all the existing Nodes
    GRAPH.delete_all()
except:
    DB_FLAG = 1

# Adding Questions and their individual Labels
QUESTION_LABEL = 'Question'

QUESTION_1 = {
    'label': QUESTION_LABEL,
    'properties': {
        'id': 1,
        'title': 'What is your E-Mail?'
    }
}

QUESTION_2 = {
    'label': QUESTION_LABEL,
    'properties': {
        'id': 2,
        'title': 'Who helped you this week?'
    }
}

QUESTION_3 = {
    'label': QUESTION_LABEL,
    'properties': {
        'id': 3,
        'title': 'Whom did you help this week?'
    }
}

QUESTION_4 = {
    'label': QUESTION_LABEL,
    'properties': {
        'id': 4,
        'title': 'What technologies did you learn?'
    }
}

question1_node = Node(QUESTION_LABEL, **QUESTION_1['properties'])
question2_node = Node(QUESTION_LABEL, **QUESTION_2['properties'])
question3_node = Node(QUESTION_LABEL, **QUESTION_3['properties'])
question4_node = Node(QUESTION_LABEL, **QUESTION_4['properties'])

node_list = [question1_node, question2_node, question3_node, question4_node]
for node in node_list:
    GRAPH.create(node)

app = FastAPI()


@app.get("/")
def read_root():
    "Returns the Message for Mock Data"
    return {"msg": "Mock Data for the Survey"}


@app.get("/graph")
def db_auth():
    "Returns if the Database Connection is Successful or not"
    if DB_FLAG == 0:
        return {"msg": "Database Connection Authenticated"}
    else:
        return {"msg": "Database Connection Refused"}


@app.get("/questions/{question_id}")
def get_questions(question_id: int):
    if question_id == 1:
        question_response = json.dumps(QUESTION_1)
    elif question_id == 2:
        question_response = json.dumps(QUESTION_2)
    elif question_id == 3:
        question_response = json.dumps(QUESTION_3)
    elif question_id == 4:
        question_response = json.dumps(QUESTION_4)
    else:
        return {"msg": "Not a valid Question ID"}

    return question_response


if __name__ == "__main__":
    uvicorn.run(
        app,
        access_log=False,
        port=5000,
        debug=True,
        reload=True
    )
