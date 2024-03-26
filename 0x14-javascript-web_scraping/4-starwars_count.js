#!/usr/bin/node
const REQ = require('request');
const URL = process.argv[2];
const ID = 18;
const urlPeople = `https://swapi-api.alx-tools.com/api/people/${ID}/`;
REQ(urlPeople, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    const numberOfMovies = json.films.length;
    console.log(numberOfMovies);
  }
});
