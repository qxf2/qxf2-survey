const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { addMocksToSchema } = require ('@graphql-tools/mock');
const { makeExecutableSchema } =  require('@graphql-tools/schema');
const fs = require('fs');
require('dotenv').config();

const typeDefs = `#graphql
  type Query {
    resolved: String
    allEmployees: EmployeesConnection
  }
  
  type Mutation {
    auth(username: String, password: String): Auth
  }

  type Auth {
    accessToken: String
    refreshToken: String
  }

  type EmployeesConnection {
    edges: [EmployeeEdge]
    node: [Employee]
  }

  type EmployeeEdge {
    node: Employee
  }

  type Employee {
    email: String
    employeeId: String
    dateJoined: String
    isActive: String
    blogAuthorName: String
    firstname: String
    lastname: String
  }
`;

const resolvers = {
    Query: {
      resolved: () => 'Resolved',
      allEmployees: (root, args, context) => {
        if (context.token != `Bearer ${process.env.ACCESS_TOKEN}`) {
          throw new Error('Unauthorized');
        }
        return employees;
      },
    },
    Mutation: {
      auth: (_, { username, password }) => {
        if (username === process.env.GRAPHQL_USERNAME && password === process.env.GRAPHQL_PASSWORD) {
          return {
            accessToken: process.env.ACCESS_TOKEN,
            refreshToken: process.env.REFRESH_TOKEN
          };
        } else {
          return {
            accessToken: null,
            refreshToken: null
          };
        }
      },
    },
  };

let employees = [];

fs.readFile('./employee-data.json', 'utf-8', (err, data) => {
  if (err) throw err;
  employees = JSON.parse(data);
});

const mocks = {
  Employee: () => employees,
  EmployeesConnection: () => ({
    edges: employees.map(employee => ({ node: employee }))
  }),
  Auth: () => ({
    accessToken: 'eyJ0f',
    refreshToken: 'eyJ0e'
  })
};

const server = new ApolloServer({
    schema: addMocksToSchema({
      schema: makeExecutableSchema({ typeDefs, resolvers }),
      mocks,
      preserveResolvers: true,
    }),
  });
  
  const { url } = startStandaloneServer(server, {
      context: async ({ req, res }) => {
        const token = req.headers.authorization || '';
        return { token };
      },
      listen: { port: 4000 }
    });
  
console.log(`🚀 Server listening at: ${url}`);
