# Qxf2 Survey App
This is a survey app designed to help keep track of the interactions by employees in Qxf2 Services, as well as the technologies they have learned. It is built with a React frontend, the backend is implemented using Python and FastAPI, and the database used to store the responses is Neo4j.

### Setup

1. Clone this repo
2. Download and install [docker](https://www.docker.com) on your machine.
3. Run the docker service and use command `docker --version` to make sure docker has been properly setup.
4. `CD` into the `qxf2-survey`repository
5. Rename `.env.example` file in the root directory to `.env`
6. You can modify the values of variables in the `.env` as per the instructions given in the `.env` file
7. Run the command `docker-compose up`. This would setup the docker containers, it would usually take 1-2 minutes.
8. Once the Docker containers are configured, you will receive a message that reads "Compiled successfully!" 
9. *Note*: Incase you change the database password in your .env file after spinning up the container for the first time, you need to rebuild the container and clear the volume. This is because `NEO4J_AUTH` has no effect because that database already has a password. You can use the following docker command
```
 docker-compose down --volumes && docker-compose build --no-cache && docker-compose up
```


### Usage
Open a browser and visit the following links.
1. http://localhost:7474 : This is the interface for Neo4j database. Try logging in to the database with the `DATABASE_USERNAME` and `DATABASE_PASSWORD` that was set in the `.env` file.
    > Try the following query to return all the users in database:
    ```
    MATCH (e:Employees)
    RETURN e. fullName, e.ID, e.email
    ```
2. http://localhost:8000/docs : This is the FastAPI swagger UI. You can try authenticating it with the `API_KEY` value that you had set in the `.env` file. You can then call any of the API endpoints to perform the desired action.
3. http://localhost:5000/graphql : This is the web interface for Graphql Qxf2 Employee database. https://github.com/qxf2/qxf2-employees. 
    > Try the following query:
    ```
    mutation {
        auth(password: "<GRAPHQL_PASSWORD set in .env>", username: "<GRAPHQl_USERNAME set in .env>") {
            accessToken
            refreshToken
            }
    }
    ```
    > If all goes well, it will return an <acessToken> in the field - copy it
    > Use a browser plugin to modify your header. Add a `Authorization` key and set it to `Bearer <accessToken>` where `accessToken` is the token you copied in previous step.
    >Query all the employees
    ```
    query findAllEmployees{
        allEmployees{
            edges{
                node{
                    email
                    employeeId
                    dateJoined
                    isActive
                    blogAuthorName
                }
            }
        }
    }

    ```
4. http://localhost:3000 : This is the web interface for the frontend React application. You can click the drop-downs to verify if the employees are displayed and syncs the employees returned from the query to fetch all employees in the previous step.

