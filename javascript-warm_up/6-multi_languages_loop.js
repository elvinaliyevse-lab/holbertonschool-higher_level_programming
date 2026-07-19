#!/usr/bin/node

const phrases = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';

for (let index = 0; index < phrases.length; index += 1) {
  output += phrases[index] + ((index < phrases.length - 1) ? '\n' : '');
}

console.log(output);
