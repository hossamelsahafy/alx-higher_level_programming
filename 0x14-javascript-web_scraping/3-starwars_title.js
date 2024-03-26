#!/usr/bin/node
const REQ = require('request');
const ID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;
REQ(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
