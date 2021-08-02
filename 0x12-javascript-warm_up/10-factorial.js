#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);

function factor (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n === 0) {
    return (1);
  } else {
    return (n * factor(n - 1));
  }
}

const value = factor(num);
console.log(value);
