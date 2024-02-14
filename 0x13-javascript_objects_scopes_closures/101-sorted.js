#!/usr/bin/node
const { dict } = require('./101-data.js');
const ND = {};
for (const k in dict) {
  const v = dict[k];
  if (!ND[v]) {
    ND[v] = [];
  }
  ND[v].push(k);
}
console.log(ND);
