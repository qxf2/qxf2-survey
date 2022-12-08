#Backup and restore Neo4j database
The scripts in this directory are used to backup the Neo4j database and restoring the backup
##WARNING:## The restore script deletes all records in the existin database.Never run against production

##neo4j_json_backup.py:
- This script is used to backup the neo4j database using the `neo4j-backup` python library https://pypi.org/project/neo4j-backup/
- To run this script:
    1. Install the requirements from the `requirements.txt` file which can be found in the `backend` directory 
    2. `CD` into the `backend/db_backup_and_restore` directory
    3. Run command `python neo4j_json_backup.py --database_name <database name> --save_dir <directory name>`
    4. You should see a new archive file in your `backend/db_backup_and_restore` directory
    5. By default the `database_name` is taken as `neo4j` and save_dir is named `synthetic_data`
    6. For help, run the command `python neo4j_json_backup.py -h`

##neo4j_restore.py:
- This script is used to restore the neo4j database using the `neo4j-backup` python library https://pypi.org/project/neo4j-backup/
- The script unzips the contents of the archive file, clears all the records in the existing database and imports the backup data 
- To run this script:
    1. Install the requirements from the `requirements.txt` file which can be found in the `backend` directory
    2. Run command `python neo4j_json_backup.py --database_name <database name> --import_file <path to import file>`
    3. Provide the name of your database with --database_name argument and the path to your zip file to be imported with the --import_file argument
    4. By default the `database_name` is taken as `neo4j` and import_file is `synthetic_data.zip`
    5. For help, run the command `python neo4j_restore.py -h`
