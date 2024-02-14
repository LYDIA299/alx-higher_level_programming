#!/usr/bin/node
const { argv } = require('node:process');
const size = argv.length;
if (size <= 3) {
  console.log(0);
} else {
  const args = argv.sort((a, b) => a - b);
  console.log(args[size - 2]);
}
