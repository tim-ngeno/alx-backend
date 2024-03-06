import redis from 'redis';

const client = redis.createClient();


// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the sever:', err);
});

client.hset('HolbertonSchools', 'Portland', 50, 'Seattle', 80, 'New'
	    + ' York', 20, 'Bogota', 20, 'Cali', 40, 'Paris', 2,
	    redis.print);

client.hgetall('HolbertonSchools', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
