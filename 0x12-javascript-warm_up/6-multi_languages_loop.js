#!/usr/bin/node
// script that prints 3 lines: (like 1-multi_languages.js)
// but by using an array of string and a loop
const firstline = 'C is fun';
const secondline = 'Python is cool';
const thirdline = 'JavaScript is amazing';

const languages = [firstline, secondline, thirdline];
for (const language of languages) {
  console.log(language);
}
