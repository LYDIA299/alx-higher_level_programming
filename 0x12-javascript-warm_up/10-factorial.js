#!/usr/bin/node
const num = parseInt(process.argv[2]);
function fact (x) {
  if (x <= 1 || isNaN(x)) {
    return (1);
  } else {
    return (x * fact(x - 1));
  }
}
console.log(fact(num));
