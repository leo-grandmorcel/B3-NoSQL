const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const redis = require('redis');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

const client = redis.createClient(6379);

client.on('error', (err) => {
  console.log('Redis Client Error', err);
});

client.on('ready', () => {
  console.log('Redis is ready');
});

app.use(express.static('public'));

const clients = new Set();

wss.on('connection', (ws) => {
  clients.add(ws);

  ws.on('message', (message) => {
    // Save the message to Redis
    client.rpush('messages', message);

    // Broadcast the message to all connected clients
    clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });

  // Retrieve chat history from Redis and send it to the new client
  client.lrange('messages', 0, -1, (err, messages) => {
    if (!err) {
      messages.forEach((message) => {
        ws.send(message);
      });
    }
  });

  ws.on('close', () => {
    clients.delete(ws);
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
