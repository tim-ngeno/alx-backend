import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';
import express from 'express';

const client = redis.createClient();
const queue = kue.createQueue();
const app = express();

client .on('error', (err) => {
  console.error('Redis error:', err);
});


const reserveSeat = (number) => {
  client.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.get).bind(client);
  const availableSeats = await getAsync('available_seats');
  return parseInt(availableSeats) || 0;
};

reserveSeat(50);

let reservationEnabled = true;


// Route to get current available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});


// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            console.error(`Seat reservation job ${job.id} failed: ${err.message}`);
            return res.json({ status: 'Reservation failed' });
        }
        console.log(`Seat reservation job ${job.id} created`);
        res.json({ status: 'Reservation in process' });
    });
});

// Route to process the queue
// Route to process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }
    reserveSeat(availableSeats - 1);
    if (availableSeats - 1 === 0) {
      reservationEnabled = false;
    }
    console.log(`Seat reservation job ${job.id} completed`);
    done();
  });
});

// Start the server
const port = 1245;
app.listen(port, () => {
  console.log(`Server started at port ${port}`);
});
