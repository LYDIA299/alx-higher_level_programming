#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    if (list[i] === searchElement) {
      nb++;
    }
  }
  return nb;
};
