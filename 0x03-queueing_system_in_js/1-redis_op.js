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


// Function to set a new school
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log('Reply:', reply);
    }
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });

}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
