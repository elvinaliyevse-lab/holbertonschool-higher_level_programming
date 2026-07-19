#!/usr/bin/node

const numbers = process.argv.slice(2).map((value) => parseInt(value, 10));
const uniqueNumbers = [...new Set(numbers)];

if (uniqueNumbers.length < 2) {
  console.log(0);
} else {
  uniqueNumbers.sort((a, b) => b - a);
  console.log(uniqueNumbers[1]);
}
