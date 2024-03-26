#!/usr/bin/node
const REQ = require('request');
const ID = 18;
const urlFilms = 'https://swapi-api.alx-tools.com/api/films/';

REQ(urlFilms, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const json = JSON.parse(body);
    let movieCount = 0;
    for (const film of json.results) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${ID}/`)) {
        movieCount++;
      }
    }

    console.log(movieCount);
  }
});
