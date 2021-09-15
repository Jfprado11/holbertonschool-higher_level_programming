#!/usr/bin/node

const url = process.argv[2];

const request = require("request");
request.get({ url: url, json: true }, function (error, r, body) {
  if (error) {
    console.error(error);
  }
  const result = {};
  for (const user of body) {
    if (!(user.userId in result) && user.completed) {
      result[user.userId] = 0;
    }
    if (user.completed === true) {
      result[user.userId] += 1;
    }
  }
  console.log(result);
});
