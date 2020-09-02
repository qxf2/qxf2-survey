"""
Sample Endpoint for Qxf2 Survey Application
"""

from fastapi import FastAPI
from py2neo import Node, Graph, Relationship, PropertyDict
from decouple import config
import uvicorn
import json

host = config("DATABASE_HOST")
username = config("DATABASE_USERNAME")
password = config("DATABASE_PASSWORD")
try:
    graph = Graph(host, auth=(username, password))
    db_flag=0
except:
    db_flag=1
     
graph.delete_all()
question_label = 'Question'

question_1 = {
    'label': 'question1',
    'properties' : {
        'id': 1,
        'title': 'What is your E-Mail?'
    }
}

question_2 = {
    'label': 'question2',
    'properties' : {
        'id': 2,
        'title': 'Who helped you this week?'
    }
}

question_3 = {
    'label': 'question3',
    'properties' : {
        'id': 3,
        'title': 'Whom did you help this week?'
    }
}

question_4 = {
    'label': 'question4',
    'properties' : {
        'id': 4,
        'title': 'What technologies did you learn?'
    }
}

app = FastAPI()
@app.get("/")
def read_root():
    "Returns the Message for Mock Data"
    return {"msg": "Mock Data for the Survey"}
@app.get("/graph")
def db_auth():
    "Returns if the Database Connection is Successful or not"
    if db_flag == 0:
        return {"msg": "Database Connection Authenticated"}
    else: 
        return {"msg": "Database Connection Refused"}
    
@app.get("/questions/{question_id}")
def read_root(question_id: int):
    question1_node = Node(question_label, **question_1['properties'])
    question2_node = Node(question_label, **question_2['properties'])
    question3_node = Node(question_label, **question_3['properties'])
    question4_node = Node(question_label, **question_4['properties'])
    
    node_list = [question1_node, question2_node, question3_node, question4_node]
    for node in node_list:
        graph.create(node)
    if (question_id == 1):
        q1 = json.dumps(question_1)
        return q1
    elif (question_id == 2):
        q2 = json.dumps(question_2)
        return q2
    elif (question_id == 3):
        q3 = json.dumps(question_3)
        return q3 
    elif (question_id == 4):
        q4 = json.dumps(question_4)
        return q4
    else:
        return {"msg": "Not a valid Question ID"}

if __name__ == "__main__":
    uvicorn.run(
        app,
        access_log=False,
        port=5000,
        debug=True,
        reload=True
    )
