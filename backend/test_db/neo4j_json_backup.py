"""
Backup Neo4j database
"""
from neo4j import GraphDatabase
from neo4j_backup import Extractor
from decouple import config

# Grabbing environment variables
HOSTNAME = config("DATABASE_HOST")
USERNAME = config("DATABASE_USERNAME")
PASSWORD = config("DATABASE_PASSWORD")

if __name__ == "__main__":

    #Add command line arguments to fetch import file and database name
    parser = argparse.ArgumentParser()

    #Command line argument to fetch database name. Database name is taken as 'neo4j' if no argument is specified
    parser.add_argument("database_name", type=str, help="Provide the name of the database",
                        nargs='?', default="neo4j", const=0)
    args = parser.parse_args()
    database = args.database_name
    encrypted = False
    trust = "TRUST_ALL_CERTIFICATES"
    driver = GraphDatabase.driver(HOSTNAME, auth=(USERNAME, PASSWORD), encrypted=encrypted, trust=trust)
    project_dir = "synthetic_data"
    input_yes = False
    compress = True

    #Extract data from database and store the backup
    extractor = Extractor(project_dir=project_dir, driver=driver, database=database,
                          input_yes=input_yes, compress=compress)
    extractor.extract_data()