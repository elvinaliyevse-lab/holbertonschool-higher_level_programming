#!/usr/bin/node

const count = parseInt(process.argv[2], 10);
const message = 'C is fun';

if (Number.isNaN(count)) {
  console.log('Missing number of occurrences');
} else if (count > 0) {
  for (let repeat = 0; repeat < count; repeat += 1) {
    console.log(message);
  }
}
