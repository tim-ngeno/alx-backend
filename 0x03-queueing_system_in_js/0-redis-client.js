import redis from 'redis';

const client = redis.createClient();

// Handle successful redis connection to server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle redis connection error
client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err);
});
