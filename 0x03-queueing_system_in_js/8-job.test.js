import chai from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const expect = chai.expect;
const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    // Enter test mode and prevent actual job processing
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode after each test
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Verify the number of jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Verify the job data
    const firstJobData = queue.testMode.jobs[0].data;
    expect(firstJobData).to.have.property('phoneNumber', '4153518780');
    expect(firstJobData).to.have.property('message', 'This is the code 1234 to verify your account');

    const secondJobData = queue.testMode.jobs[1].data;
    expect(secondJobData).to.have.property('phoneNumber', '4153518781');
    expect(secondJobData).to.have.property('message', 'This is the code 4562 to verify your account');
  });
});
