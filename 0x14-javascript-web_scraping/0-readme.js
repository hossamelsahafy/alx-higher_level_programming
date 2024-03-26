#!/usr/bin/node
const fs = require('fs')
let filePath = process.argv[2]
fs.readFile(filePath, 'utf8', function(err, data) {
    if (err) {
        console.error(err)
    }
    else {
        console.log(data)
    }
});
