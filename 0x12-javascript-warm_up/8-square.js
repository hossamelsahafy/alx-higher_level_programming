#!/usr/bin/node
// script that prints a square
const size = process.argv[2];
if (size % 1 !== 0) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  let l = '';
  for (let j = 0; j < size; j++) {
    l += 'X';
  }
  console.log(l);
}
