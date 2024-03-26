#!/usr/bin/node
const REQ = require('request');
const URL = process.argv[2];
REQ(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const Completed = {};
    for (const Todo of todos) {
        if (Todo.completed) {
            if(Completed[Todo.userId]) {
                Completed[Todo.userId]++;
            } else {
                Completed[Todo.userId] = 1;
            }
        }
    }
        console.log(Completed);
    }
});
