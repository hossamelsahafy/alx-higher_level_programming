#!/usr/bin/node
// script that prints two arguments passed to it,
// in the following format: “ is ”
if (process.argv.length < 3) {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
} else if (process.argv.length > 3) {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
} else {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
}
