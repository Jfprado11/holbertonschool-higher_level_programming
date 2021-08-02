#!/usr/bin/node
const args = process.argv;

const num = parseInt(args[2]);

if (isNaN(num) || !args[2]) {
  console.log('Not a number');
} else {
  console.log('my number:', num);
}
