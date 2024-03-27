#!/usr/bin/node
const fetch = require('node-fetch');
const movieId = process.argv[2];

async function getCharacterNames (movieId) {
  const response = await fetch(`https://swapi.dev/api/films/${movieId}/`);
  const data = await response.json();
  const characterUrls = data.characters;
  for (const url of characterUrls) {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data.name);
  }
}

getCharacterNames(movieId);
