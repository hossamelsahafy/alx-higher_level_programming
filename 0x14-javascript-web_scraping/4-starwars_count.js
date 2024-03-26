#!/usr/bin/node
const REQ = require('request');
const urlPeople = 'https://swapi-api.alx-tools.com/api/people/18/';
REQ(urlPeople, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    const numberOfMovies = json.films.length;
    console.log(numberOfMovies);
  }
});
