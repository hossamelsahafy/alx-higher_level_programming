#!/usr/bin/node
// script that prints two arguments passed to it,
// in the following format: “ is ”
const i = parseFloat(process.argv[2]);
if (i % 1 === 0) {
  console.log(`My number: ${process.argv[2]}`);
} if (i % 1 !== 0) {
  console.log('Not a number');
}
