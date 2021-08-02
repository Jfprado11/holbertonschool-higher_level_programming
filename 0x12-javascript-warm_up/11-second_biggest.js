#!/usr/bin/node

const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 0; i < args.length; i++) {
    if (!isNaN(parseInt(args[i]))) {
      arr.push(args[i]);
    }
  }
  const large = Math.max(...arr);
  const index = arr.indexOf(large);
  arr.splice(index, 1);
  seconLarge = Math.max(...arr);
  console.log(seconLarge);
}
