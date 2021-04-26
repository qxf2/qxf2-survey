# Survey App - Qxf2

A Full Stack Application developed using React, FastAPI and Neo4j to make Qxf2 a fairer place to work.

## Stack

- [React](https://reactjs.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Neo4j](https://neo4j.com/)
- [Github Actions](https://github.com/features/actions)
- [AWS EC2](https://aws.amazon.com/ec2/)

## Installation

### Setting up Frontend

1. Clone the Repository.
2. `cd` into the `frontend	` directory.
3. Install NodeJS from here: https://nodejs.org/en/
4. Ensure that NodeJS and NPM has been installed by running the following command: `node --version` and `npm --version`
5. If a specific version is popped up, run the command: `npm install` to install all dependencies.
6. Rename the `.env.expample` file to `.env` and enter a key of your choice for the `REACT_APP_API_KEY`
7. Run the command: `npm start` to kick-start the Application. It will take a couple of seconds to setup the development server on Port 3000.
8. To build the Application run the command: `npm build`.

### Setting up the Database

- Setup Neo4j Desktop.
- Create a new Project and a new Database.
- Keep the Username for the database as `neo4j` and password as per your choosing.
- To migrate the database from quilt to neo4j go to `Migrate Quilt to Neo4j` section

### Migrate Quilt to Neo4j

#### Prerequisites
---
1. Install [Neo4j Desktop](https://neo4j.com/download-v2/)
2. Create a new project and add a local database. Set the database name as `neo4j` and any password of your choice.Note down the name and password of your database
3. Click on the `...` option on your database and select `Manage`
4. Go to Settings tab
5. Find `dbms.directories.import` and assign it the path of `migrations` folder
   (ex: *C:/Users/xyz/Desktop/qxf2-survey/backend/app/db/migrations*)
6. Now, go to `Details` tab
7. Start the database
8. Copy  `Bolt Port`


#### How to Run?
---
1. Clone this repo
2. cd into the `backend` directory.
3. Setup a virtual environment and activate it
4. Install the requirements with `pip install -r requirements.txt`
5. In your backend directory rename `.env.example` to `.env`
6. Open `.env` file and assign the values to the environment variable as follows:
    ```
    DATABASE_USERNAME = "neo4j"
    DATABASE_PASSWORD = "<Prerequisites: Step 2>"
    DATABASE_HOST = "<Prerequisites: Step 8>"
    API_KEY = ""
    PROJECT_NAME = ""
    ```
7. Make sure you have the quilt package `qxf2/dev_survey` installed
8. Run `backend/app/db/migrations/quilt2neo4j.py` - which generates the required csv files
9. Run `backend/app/db/init_db.py` - which imports the generated csv files
10. Go back to Neo4j Desktop.
11. Click on Open to launch neo4j browser.
12. Click on Database icon to see the database information.
13. If you see the 2 Node Lables and  3 Relationship Types, the quilt database is succesfully migrated to neo4j.


### Setting up Backend

1. `cd` into the `backend` directory
2. Setup and activate a virtual environment
3. Run the command to install all packages: `pip install -r requirements.txt`
4. Rename the `.env.example` in `backend` directory as `.env`
5. Open `.env` file and assign the values to the environment variable as follows:
    ```
    DATABASE_USERNAME = "neo4j"
    DATABASE_PASSWORD = "<Password of your database>"
    DATABASE_HOST = "<bolt port of your database>"
    API_KEY = "<Should be same  as REACT_APP_API_KEY set in the frontend .env file>"
    PROJECT_NAME= "<any>"
    ```
6. `cd` into the `app` directory
7. Kick-Start the Application with the following command: `uvicorn main:app --reload`



