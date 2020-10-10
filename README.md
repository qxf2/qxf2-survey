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

- Clone the Repository.
- `cd` into the `frontend	` directory.
- Ensure that NodeJS and NPM has been installed by running the following command: `node --version` and `npm --version`
- If a specific version is popped up, run the command: `npm install` to install all dependencies. 
- Run the command: `npm start` to kick-start the Application. It will take a couple of seconds to setup the development server on Port 3000.
- To build the Application run the command: `npm build`.

### Setting up Backend 

- Clone the Repository.
- Install a Virtual Environment using the command: `pip install virtualenv`
- Setup the Virtual Environment by running the command: `virtualenv env`
- Kick-start the Virtual Environment by running the command: `env\Scripts\activate`
- Run the command to install all packages: `pip install -r requirements.txt`
- Kick-Start the Application with the following command: `uvicorn main:app --reload`

### Setting up the Database 

- Setup Neo4j Desktop.
- Create a new Project and a new Database. 
- Keep the Username as default `neo4j` and password as per your choosing. 
- Start the Database and keep a note of the Username and Password along with the Port on which the Database is running.
-  Rename the `.env.example` as `.env` and fill all the necessary parameters there. 
- Run the API endpoint `/graph` on the FastAPI to check if the Database Connection is authenticated. 

