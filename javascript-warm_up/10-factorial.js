#!/usr/bin/node

function factorial (integer) {
  if (integer === 1 || Number.isNaN(integer) || integer === 0) {
    return 1;
  }
  return integer * factorial(integer - 1);
}

const number = parseInt(process.argv[2], 10);
console.log(factorial(number));
