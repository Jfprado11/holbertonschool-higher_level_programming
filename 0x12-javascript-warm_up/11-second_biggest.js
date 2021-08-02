#!/usr/bin/node

const args = process.argv;

if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  const arr = [];
  for (let x = 0; x < args.length; x++) {
    if (!isNaN(parseInt(args[x]))) {
      arr.push(parseInt(args[x]));
    }
  }
  arr.sort();
  for (let i = arr.length - 2; i >= 0; i--) {
    if (arr[i] !== arr[arr.length - 1]) {
      console.log(arr[i]);
      break;
    }
  }
}
