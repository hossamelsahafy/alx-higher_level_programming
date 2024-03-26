#!/usr/bin/node
const REQ = require('request');
const URL = process.argv[2];

REQ(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
