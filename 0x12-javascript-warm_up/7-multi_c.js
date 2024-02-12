#!/usr/bin/node
// script that prints x times “C is fun”
const times = process.argv[2];
if (times % 1 !== 0) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < times; i++) {
  console.log('C is fun');
}
