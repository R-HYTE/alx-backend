import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0123456789',
  message: 'Hey, this is from the job creator!',
};

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', function () {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', function () {
  console.log('Notification job completed');
});

job.on('failed', function () {
  console.log('Notification job failed');
});

job.save(function (err) {
  if (err) {
    console.error(`Error creating job: ${err}`);
    return;
  }
});
