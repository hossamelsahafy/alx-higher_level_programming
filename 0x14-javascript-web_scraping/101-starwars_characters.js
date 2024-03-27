#!/usr/bin/node
const request = require('request-promise-native');
const movieId = process.argv[2];
function getCharacterNames (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url)
    .then(body => {
      const data = JSON.parse(body);
      const characterUrls = data.characters;
      const characterPromises = characterUrls.map(url => request(url));

      Promise.all(characterPromises)
        .then(characterBodies => {
          characterBodies.forEach(characterBody => {
            const character = JSON.parse(characterBody);
            console.log(character.name);
          });
        })
        .catch(error => console.log(error));
    })
    .catch(error => console.log(error));
}

getCharacterNames(movieId);
