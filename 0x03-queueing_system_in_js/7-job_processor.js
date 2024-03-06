import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  // Track the progress of the job
  job.progress(0, 100);

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    // Track progress to 50%
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber} with message:`
		+ ` ${message}`);
    done();
  }
}

const queue = kue.createQueue();

// Process the queue with 2 jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call sendNotification with the provided args
  sendNotification(phoneNumber, message, job, done);
});
