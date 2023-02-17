const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { addMocksToSchema } = require ('@graphql-tools/mock');
const { makeExecutableSchema } =  require('@graphql-tools/schema');
const { GraphQLError } = require('graphql');
const fs = require('fs');
require('dotenv').config();

const typeDefs = `#graphql
  type Query {
    allEmployees: Employees
  }
  
  type Mutation {
    auth(username: String, password: String): Auth
  }

  type Auth {
    accessToken: String
    refreshToken: String
  }

  type Employees {
    edges: [EmployeeEdge]
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
      allEmployees: (root, args, context) => {
        if (context.token != `Bearer ${process.env.ACCESS_TOKEN}`) {
          throw new GraphQLError("object of type 'AuthInfoField' has no len()", {
            extensions: {
              code: 'Unauthorized'
            },
          });
      }
      },
    },
    Mutation: {
      auth: (_, { username, password }) => {
        if (username === process.env.GRAPHQl_USERNAME && password === process.env.GRAPHQL_PASSWORD) {
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
  Employees: () => ({
    edges: employees.map(employee => ({ node: employee }))
  }),
};

const server = new ApolloServer({
    schema: addMocksToSchema({
      schema: makeExecutableSchema({ typeDefs, resolvers }),
      mocks,
      preserveResolvers: true,
    }),
    includeStacktraceInErrorResponses: false
  });

const server_port = 4000
const { url } = startStandaloneServer(server, {
    context: async ({ req, res }) => {
      const token = req.headers.authorization || '';
      return { token };
    },
    listen: { port: server_port },
  });
  
console.log(`🚀 Server listening at Port: ${server_port}`);
