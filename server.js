const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');

const app = express();
app.use(express.json());

// --- REST ENDPOINTS ---
app.get('/api/v1/health', (req, res) => {
  res.status(200).json({ status: 'UP', timestamp: new Date() });
});

// Endpoint con falla simulada (1 de cada 3 peticiones falla)
let requestCount = 0;
app.get('/api/v1/users', (req, res) => {
  requestCount++;
  if (requestCount % 3 === 0) {
    return res.status(500).json({ error: 'Internal Database Connection Timeout' });
  }
  res.status(200).json([{ id: 1, name: 'John Doe', role: 'Admin' }]);
});

// --- GRAPHQL ENDPOINT ---
const schema = buildSchema(`
  type SystemStatus {
    service: String!
    healthy: Boolean!
    latencyMs: Int!
  }
  type Query {
    checkService(name: String!): SystemStatus
  }
`);

const root = {
  checkService: ({ name }) => {
    return {
      service: name,
      healthy: true,
      latencyMs: Math.floor(Math.random() * 100) + 10
    };
  }
};

app.use('/graphql', graphqlHTTP({
  schema: schema,
  rootValue: root,
  graphiql: true,
}));

app.listen(4000, () => console.log('Mock Server running on http://localhost:4000'));