#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

const request = require('request');
request.get({ url: url, json: true }, function (error, r, body) {
  if (error) {
    console.error(error);
  }
  console.log(body.title);
});
