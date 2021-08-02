#!/usr/bin/node
const args = process.argv;

const num = parseInt(args[2]);

if (isNaN(num) || !args[2]) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let arr = 'X';
    for (let x = 1; x < num; x++) {
      arr = arr + 'X';
    }
    console.log(arr);
  }
}
