#!/usr/bin/node
const REQ = require('request');
const FS = require('fs');
const URL = process.argv[2];
const Path = process.argv[3];
REQ(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    FS.writeFile(Path, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
