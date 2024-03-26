#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  } else {
    process.stdout.write(data);
  }
});
