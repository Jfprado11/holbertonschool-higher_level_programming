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
  function secondMax (arr) {
    firstLarge = Math.max(...arr);
    index = arr.indexOf(firstLarge);
    arr.splice(index, 1);
    secondLarge = Math.max(...arr);
    return (secondLarge);
  }
  arr.sort();
  console.log(secondMax(arr));
}