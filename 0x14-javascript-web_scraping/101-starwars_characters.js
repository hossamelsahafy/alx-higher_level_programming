#!/usr/bin/node
const request = require('request-promise');
const movieId = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function getCharacters() {
  try {
    const body = await request(URL);
    const data = JSON.parse(body);
    const characterURLS = data.characters;

    for (let url of characterURLS) {
      const body = await request(url);
      const character = JSON.parse(body);
      console.log(character.name);
    }
  } catch (error) {
    console.log(error);
  }
}

getCharacters();
