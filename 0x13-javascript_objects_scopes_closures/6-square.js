#!/usr/bin/node
const Squ = require('./5-square');

module.exports = class Square extends Squ {
  charPrint (c) {
    let x;
    if (c === undefined) {
      x = 'X';
    } else {
      x = 'C';
    }
    for (let i = 0; i < this.height; i++) {
      let arr = x;
      for (let j = 1; j < this.width; j++) {
        arr = arr + x;
      }
      console.log(arr);
    }
  }
};
