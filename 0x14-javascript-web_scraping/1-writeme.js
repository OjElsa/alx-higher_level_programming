#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file path> "<string to write>"');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  } else {
    console.log(`Content has been written to ${filePath}`);
  }
});