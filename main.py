"""
Sample Endpoint for Qxf2 Survey Application
"""

from fastapi import FastAPI
from py2neo import Graph
from decouple import config
import uvicorn

app = FastAPI()
@app.get("/")
def read_root():
    "Returns the Message for Mock Data"
    return {"msg": "Mock Data for the Survey"}
@app.get("/graph")
def db_auth():
    "Returns if the Database Connection is Successful or not"
    host = config("DATABASE_HOST")
    username = config("DATABASE_USERNAME")
    password = config("DATABASE_PASSWORD")
    try:
        graph = Graph(host, auth=(username, password))
        return {"msg": "Database Connection Successful"}
    except:
        return {"msg": "Database Connection Unsuccessful"}

if __name__ == "__main__":
    uvicorn.run(
        app,
        access_log=False,
        port=5000,
        debug=True,
        reload=True
    )
    