#!/usr/bin/node
const { argv } = require('node:process');

const add = (a, b) => console.log(a + b);

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
add(a, b);
