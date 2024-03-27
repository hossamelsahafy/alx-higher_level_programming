#!/usr/bin/node
const REQ = require('request-promise-native');
async function getCharacterNames() {
    try {
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

getCharacterNames();
