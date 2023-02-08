const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const { addMocksToSchema } = require ('@graphql-tools/mock');
const { makeExecutableSchema } =  require('@graphql-tools/schema');
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

const employees = [
{
    email: 'generoustaker@qxf2.com',
    employeeId: '2',
    dateJoined: '01-Apr-1970',
    isActive: "Y",
    blogAuthorName: 'user1',
    firstname: 'Generous',
    lastname: 'Taker'
},
{
    email: "inactive_user@qxf2.com",
    employeeId: "3",
    dateJoined: "02-Mar-1969",
    isActive: "N",
    blogAuthorName: "user2",
    firstname: 'Inactive',
    lastname: 'User'
},
{
    email: "slow_learner@qxf2.com",
    employeeId: "5",
    dateJoined: "25-Feb-1977",
    isActive: "Y",
    blogAuthorName: "user3",
    firstname: 'Slow',
    lastname: 'Learner'
},
{
    email: "smart_learner@qxf2.com",
    employeeId: "4",
    dateJoined: "04-Sept-1976",
    isActive: "Y",
    blogAuthorName: "user4",
    firstname: 'Smart',
    lastname: 'Learner'
},
{
    email: "use_this_email_to_find_me@qxf2.com",
    employeeId: "6",
    dateJoined: "03-Aug-1980",
    isActive: "Y",
    blogAuthorName: "user5",
    firstname: 'Use my email',
    lastname: 'find me'
},
{
    email: "user_to_be_deleted@qxf2.com",
    employeeId: "7",
    dateJoined: "28-July-1975",
    isActive: "N",
    blogAuthorName: "user6",
    firstname: 'Use my ID',
    lastname: 'Delete me'
},
{
    email: "generousgiver@qxf2.com",
    employeeId: "1",
    dateJoined: "03-Dec-1980",
    isActive: "Y",
    blogAuthorName: "user7",
    firstname: 'Generous',
    lastname: 'Giver'
},
{
    email: "user_status_to_be_updated@qxf2.com",
    employeeId: "8",
    dateJoined: "15-Aug-1986",
    isActive: "N",
    blogAuthorName: "user8",
    firstname: 'Update',
    lastname: 'My Status'
}
];
    

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
