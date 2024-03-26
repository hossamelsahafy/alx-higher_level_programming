#!/usr/bin/node
const REQ = require('request');
const urlFilms = 'https://swapi-api.alx-tools.com/api/films/';
const ID = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${ID}/`;
REQ(urlFilms, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    let numberOfMovies = 0;
    json.results.forEach(film => {
      if (film.characters.includes(characterUrl)) {
        numberOfMovies++;
      }
    });
    console.log(numberOfMovies);
  }
});
