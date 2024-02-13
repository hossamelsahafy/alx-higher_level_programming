#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
function sL (args) {
  args = args.map(Number).sort((a, b) => b - a);
  return args[1] || 0;
}
console.log(sL(process.argv.slice(2)));
