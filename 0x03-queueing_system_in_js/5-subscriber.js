import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Subscribe to the channel 'holberton school channel'
  client.subscribe('holberton school channel', (err) => {
    if (err) {
      console.error('Error subscribing to channel:', err);
    }
  });
});

// Handle redis connection error
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

// Listen for messages on subscribed channel
client.on('message', (channel, message) => {
  console.log(`Message received on channel '${channel}':`, message);

  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
