#!/usr/bin/node
const { list } = require('./100-data.js');
console.log(list);
const map = list.map((x, i) => x * i);
console.log(map);
