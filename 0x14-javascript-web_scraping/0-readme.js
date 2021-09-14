#!/usr/bin/node
const fs = require("fs");

const args = process.argv;

const file = args[2];

fs.readFile(file, "utf8", (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
