# Queuing System in JavaScript with Redis and Kue

## Overview

This project demonstrates how to build a queuing system in JavaScript using Redis as the data store and Kue as the queue management system. It includes examples of basic operations with Redis, asynchronous operations, and integration with an Express.js application.

## Learning Objectives

By the end of this project, you will learn:

- How to run a Redis server on your machine
- Performing simple operations with the Redis client
- Using a Redis client with Node.js for basic operations
- Storing hash values in Redis
- Handling async operations with Redis
- Utilizing Kue as a queue system
- Building a basic Express.js app interacting with a Redis server
- Building a basic Express.js app interacting with a Redis server and queue

## Running Redis Server Locally

To run a Redis server locally, follow these steps:

1. **Install Redis:** Download and install Redis from [Redis.io](https://redis.io/download) or use a package manager.

2. **Start Redis Server:**
   - Open a terminal window.
   - Run `redis-server` command.

3. **Verify Redis Server:**
   - Open another terminal window.
   - Run `redis-cli ping` to check if the server is running.

## Redis Operations with Node.js

To perform Redis operations in Node.js, ensure you have the `redis` npm package installed:

```bash
npm install redis
```

### Example of connecting to Redis and setting/getting values:

```javascript
const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => {
  console.log('Connected to Redis server');
});

// Example: Set and Get operations
client.set('key', 'value', redis.print);
client.get('key', (err, reply) => {
  console.log('Value:', reply);
});
```

## Using Redis for Hash Values

### Redis supports storing hash values (like objects) using `hmset` and `hgetall`:

```javascript
client.hmset('user:1', {
  name: 'John Doe',
  age: 30,
});

client.hgetall('user:1', (err, user) => {
  console.log('User:', user);
});
```

## Async Operations with Redis

### Redis operations are typically asynchronous. Use promises or callbacks to handle results:

```javascript
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);

getAsync('key').then(reply => {
  console.log('Value:', reply);
}).catch(err => {
  console.error('Error:', err);
});
```

## Using Kue as a Queue System

### Install Kue and create a queue:

``` bash
npm install kue
```

```javascript
const kue = require('kue');
const queue = kue.createQueue();

// Example: Creating a job
const job = queue.create('email', {
  to: 'user@example.com',
  subject: 'Hello!',
  body: 'This is a test email',
});

job.save();

// Process jobs
queue.process('email', (job, done) => {
  sendEmail(job.data.to, job.data.subject, job.data.body, done);
});
```

## Building an Express App with Redis and Kue

### Example of an Express.js app using Redis for data storage and Kue for job processing:

```javascript
const express = require('express');
const redis = require('redis');
const kue = require('kue');

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

// Example route using Redis
app.get('/users/:id', (req, res) => {
  const userId = req.params.id;
  client.get(`user:${userId}`, (err, user) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error retrieving user');
    } else if (user) {
      res.json(JSON.parse(user));
    } else {
      res.status(404).send('User not found');
    }
  });
});

// Example route using Kue
app.post('/jobs', (req, res) => {
  const job = queue.create('task', {
    type: req.body.type,
    data: req.body.data,
  });

  job.save(() => {
    res.json({ message: 'Job created' });
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

```