#!/usr/bin/node
const fs = require('fs');

const content = process.argv[3];
const path = process.argv[2];

fs.writeFile(path, content, (err) => {
  if (err) {
    console.error(err);
  }
});
