"""
This module authenticates and connects to the neo4j database
"""

from py2neo import Graph
from decouple import config

# Grabbing environment variables
HOSTNAME = config("DATABASE_HOST")
USERNAME = config("DATABASE_USERNAME")
PASSWORD = config("DATABASE_PASSWORD")


def auth():
    "Authenticating with the Database"
    GRAPH = None
    try:
        GRAPH = Graph(HOSTNAME, auth=(USERNAME, PASSWORD))
        print("Database authenticated")
    except Exception as error:
        print("Database authentication failed", error)
    return GRAPH
