#!/usr/bin/node
const REQ = require('request-promise-native');
const movieId = process.argv[2];

async function getCharacterNames (movieId) {
  try {
    const URL = `https://swapi.dev/api/films/${movieId}/`;
    const body = await REQ(URL);
    const data = JSON.parse(body);
    const characterURLS = data.characters;

    for (const url of characterURLS) {
      const characterBody = await REQ(url);
      const character = JSON.parse(characterBody);
      console.log(character.name);
    }
  } catch (error) {
    console.log(error);
  }
}

getCharacterNames(movieId);
