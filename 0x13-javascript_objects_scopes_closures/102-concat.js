#!/usr/bin/node
const fs = require('fs');
const [fileA, fileB, fileC] = process.argv.slice(2);
const ReadA = fs.readFileSync(fileA, 'utf8');
const ReadB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, ReadA + ReadB);
