#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  arr.splice(0, arr.length);
  for (let x = list.length - 1; x > 0; x--) {
    arr.push(list[x]);
  }
  return arr;
};
