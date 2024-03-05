import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', (id) => {
  console.log(`Notification job created: ${id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save((err) => {
  if (err) {
    console.error('Error creating notification job:', err);
  }
});
