from decouple import config

USERNAME = config("GRAPHQl_USERNAME")
PASSWORD = config("GRAPHQL_PASSWORD")

authorise = f"""mutation {{
    auth(password: "{PASSWORD}", username: "{USERNAME}") {{
        accessToken
        refreshToken
        }}
    }}"""

fetch_employees = """query
    findAllEmployees{
        allEmployees{
            edges{
                node{
                    author_name: blogAuthorName
                    firstName: firstname
                    lastName: lastname
                    ID: employeeId
                    email: email
                    status: isActive
                }
            }
        }
    }"""