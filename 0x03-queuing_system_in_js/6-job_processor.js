import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);

  // Mark the job as completed
  done();
});

// On successful connection to Redis
queue.on('ready', function () {
  console.log('Kue connected to Redis');
});

// On connection error
queue.on('error', function (err) {
  console.error('Error connecting to Redis:', err);
});
