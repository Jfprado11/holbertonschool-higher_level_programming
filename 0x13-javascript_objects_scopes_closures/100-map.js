#!/usr/bin/node
const arr = require('./100-data.js').list;

const newArr = arr.map((x, index) => {
  return x * index;
});
console.log(arr);
console.log(newArr);
