#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
const request = require("request");
const fs = require("fs");
request.get({ url: url }, function (error, r, body) {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(path, body, (err) => {
    if (err) {
      console.error(err);
      return;
    }
  });
});
