#!/usr/bin/node
const REQ = require('request');
const URL = process.argv[2];
const Id = 18;
REQ(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    let numberOfMovies = 0;
    for (const Film of json.results) {
        if (Film.characters.some(character => character.includes('/18/'))) {
            numberOfMovies++;
      }
    }
    console.log(numberOfMovies);
  }
});
