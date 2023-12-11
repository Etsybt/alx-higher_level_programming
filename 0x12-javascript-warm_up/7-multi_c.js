#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(arg)) {
  const num = parseInt(arg);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
