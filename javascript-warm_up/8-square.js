#!/usr/bin/node

const size = parseInt(process.argv[2], 10);
const character = 'X';

if (Number.isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (let repeat = 0; repeat < size; repeat += 1) {
    console.log(character.repeat(size));
  }
}
