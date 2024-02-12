#!/usr/bin/env node
// Script script that prints a message depending
// of the number of arguments passed
const arg = process.argv.length - 2; // remove  the first two elements (node and this file name)
if (arg === 0) {
    console.log('No argument');
}
else if (arg === 1) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}
