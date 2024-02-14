#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let r = num; r > 0; r--) {
    let c = '';
    for (let i = num; i > 0; i--) c += 'X';
    console.log(c);
  }
}
