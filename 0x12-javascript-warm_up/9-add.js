#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const args = process.argv;

const num = parseInt(args[2]);
const numSec = parseInt(args[3]);

console.log(add(num, numSec));
