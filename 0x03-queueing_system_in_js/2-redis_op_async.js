import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

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

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }

}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
