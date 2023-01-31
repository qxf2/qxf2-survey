"""
Clear the existing database and restore the Neo4j backup 
"""
import os
import sys
from neo4j import GraphDatabase
from neo4j_backup import Importer
from py2neo import Graph
from decouple import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.db import schemas, session as db
from app.db.queries import cypher
from zipfile import ZipFile
import argparse
import shutil

GRAPH = db.auth()

# Grabbing environment variables
HOSTNAME = config("DATABASE_HOST")
USERNAME = config("DATABASE_USERNAME")
PASSWORD = config("DATABASE_PASSWORD")

#Unzip the import files
def unzip_file(IMPORT_FILE,extract_dir):
    with ZipFile(IMPORT_FILE, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()    
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall(extract_dir)
        print('Done!')

# exception handler
def handler(func, path, exc_info):
    print("Inside handler")
    print(exc_info)

#Get command line arguments
def get_arguments():
    #Add command line arguments to fetch import file and database name
    parser = argparse.ArgumentParser()
    #Command line argument to fetch import file. File name is taken as 'synthetic_data.zip' if no argument is specified
    parser.add_argument("--import_file", type=str, help="Provide the import file zip",
                        nargs='?', default="synthetic_data.zip", const=0)
    #Command line argument to fetch database name. Database name is taken as 'neo4j' if no argument is specified
    parser.add_argument("--database_name", type=str, help="Provide the name of the database",
                        nargs='?', default="neo4j", const=0)
    args = parser.parse_args()
    return args

#Imports the data extracted to the database
def import_data(extract_dir,database):
    encrypted = False
    trust = "TRUST_ALL_CERTIFICATES"
    driver = GraphDatabase.driver(HOSTNAME, auth=(USERNAME, PASSWORD), encrypted=encrypted, trust=trust)   
    input_yes = False

    #Import the data to the database
    importer = Importer(project_dir=extract_dir, driver=driver, database=database, input_yes=input_yes)
    importer.import_data()

def main():
    args = get_arguments()
    IMPORT_FILE = args.import_file
    database = args.database_name

    #Get the directory into which the archive will be extracted
    extract_dir = os.path.splitext(IMPORT_FILE)[0] 

    #Unzip the archived file
    unzip_file(IMPORT_FILE,extract_dir)

    #Clear the existing data in database
    clear_database = GRAPH.run(cypher.DELETE_ALL_RECORDS)

    #import data to database
    import_data(extract_dir,database)

    #Delete folder after importing the data
    shutil.rmtree(extract_dir, onerror=handler)

if __name__ == "__main__":
    main()


    

    