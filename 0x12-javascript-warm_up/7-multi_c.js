#!/usr/bin/node
const { argv } = require('node:process');
let num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
