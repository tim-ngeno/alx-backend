# Using Node.js and Redis for Building Scalable Applications

This guide will walk you through utilizing Node.js with Redis to build scalable applications. Redis is an in-memory data structure store known for its high performance and versatility, making it an excellent choice for caching, session management, and data storage in Node.js applications.

## Table of Contents
1. [Introduction to Redis](#introduction-to-redis)
2. [Setting up Redis](#setting-up-redis)
3. [Running Simple Operations with Redis CLI](#running-simple-operations-with-redis-cli)
4. [Using Redis Client with Node.js](#using-redis-client-with-nodejs)
5. [Storing Hash Values in Redis](#storing-hash-values-in-redis)
6. [Handling Async Operations with Redis](#handling-async-operations-with-redis)
7. [Using Kue as a Queue System](#using-kue-as-a-queue-system)

### 1. Introduction to Redis

Redis is an open-source, in-memory data structure store used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, sorted sets, and more. Redis is known for its exceptional performance and versatility, making it a popular choice for building scalable applications.

### 2. Setting up Redis

Install redis and nodejs

Start up thre redis server with `redis-server` command

### 3. Running Simple Operations with Redis CLI

Redis CLI provides a command-line interface to interact with Redis. Here are some basic operations:

```bash
# Set a key-value pair
redis-cli set mykey "Hello Redis"

# Get the value by key
redis-cli get mykey
```

### 4. Using Redis Client with Node.js

Node.js provides various Redis clients for interacting with Redis from your applications. Here's an example using `redis` npm package:

```javascript
const redis = require('redis');
const client = redis.createClient();

// Set a value
client.set('mykey', 'Hello Redis', (err, reply) => {
  console.log(reply);
});

// Get a value
client.get('mykey', (err, reply) => {
  console.log(reply);
});
```

### 5. Storing Hash Values in Redis

Redis supports hash data structures, which are useful for storing objects. Here's how you can use hashes:

```javascript
// Set hash values
client.hmset('user:1', {
  name: 'John Doe',
  email: 'john@example.com'
});

// Get hash values
client.hgetall('user:1', (err, user) => {
  console.log(user);
});
```

### 6. Handling Async Operations with Redis

Node.js applications often involve asynchronous operations. Redis commands in Node.js are typically asynchronous, and you can handle them using callbacks, promises, or async/await:

```javascript
// Using callbacks
client.set('mykey', 'value', (err, reply) => {
  console.log(reply);
});

// Using promises
client.set('mykey', 'value')
  .then(reply => console.log(reply))
  .catch(err => console.error(err));

// Using async/await
async function setValue() {
  try {
    const reply = await client.setAsync('mykey', 'value');
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
}
setValue();
```

### 7. Using Kue as a Queue System

Kue is a priority job queue for Node.js backed by Redis, allowing you to handle distributed job processing. Here's a basic example of using Kue:

```javascript
const kue = require('kue');
const queue = kue.createQueue();

// Create a job
const job = queue.create('email', {
  to: 'recipient@example.com',
  subject: 'Hello',
  body: 'This is a test email'
}).save();

// Process job
queue.process('email', (job, done) => {
  sendEmail(job.data, err => {
    if (err) return done(err);
    done();
  });
});

function sendEmail(data, callback) {
  // Send email logic
}
```

---
