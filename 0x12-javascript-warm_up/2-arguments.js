#!/usr/bin/node
// Script script that prints a message depending
// of the number of arguments passed
const arg = process.argv.length - 2; // Subtract 2 to exclude 'node' and the script filename
if (arg === 0) {
  console.log('No argument');
} else if (arg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
