#!/usr/bin/node
const REQ = require('request');
const movieId = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
REQ(URL, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const data = JSON.parse(body);
        const characterURLS = data.characters;
        characterURLS.forEach((url, index) => {
            REQ(url, (error, response, body) => {
                if (error) {
                    console.log(error);
                } else {
                    const character = JSON.parse(body);
                    console.log(character.name);
                }
            });
        });
    }
});
