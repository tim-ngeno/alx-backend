import kue from 'kue';

const queue = kue.createQueue();

export default function createPushNotificationJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  } else {
    jobs.forEach((jobData) => {
      const job = queue.create('push_notification_code_3', jobData);

      job.on('enqueue', (id) => `Notification job created: ${id}`);

      // Handle job completion
      job.on('complete', () => {
	console.log(`Notification job ${jobData.id} completed`);
      });

      job.on('failed', (err) => {
	console.log(`Notification job ${jobData.id} failed: ${err}`);
      });

      job.on('progress', (progress) => {
	console.log(`Notification job ${jobData.id} ${progress}% complete`);
      });
    });

  }
}
