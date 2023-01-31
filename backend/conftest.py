# conftest.py
#from db_backup_and_restore import neo4j_restore
import subprocess

def pytest_sessionfinish(session, exitstatus):
    if not hasattr(session.config, "workerinput"):
        subprocess.call(["python", "./db_backup_and_restore/neo4j_restore.py", "--import_file", "./db_backup_and_restore/synthetic_data.zip", "--database_name", "neo4j"], shell=True)
