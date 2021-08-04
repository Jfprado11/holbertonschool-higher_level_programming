#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocur = 0;
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      ocur = ocur + 1;
    }
  }
  return ocur;
};
