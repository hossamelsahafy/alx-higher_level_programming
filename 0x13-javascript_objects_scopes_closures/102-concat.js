#!/usr/bin/node
// Write a script that concats 2 files.
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination
const fs = require('fs');
const [fileA, fileB, fileC] = process.argv.slice(2);
const ReadA = fs.readFileSync(fileA, 'utf8');
const ReadB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, ReadA + ReadB);
