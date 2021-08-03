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
  const firstLarge = Math.max(...arr);
  const index = arr.indexOf(firstLarge);
  arr.splice(index, 1);
  const secondLarge = Math.max(...arr);
  console.log(secondLarge);
}
