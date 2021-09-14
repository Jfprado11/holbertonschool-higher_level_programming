#!/usr/bin/node

const url = process.argv[2];

const request = require('request');
request.get({ url: url, json: true }, function (error, r, body) {
  if (error) {
    console.error(error);
  }
  const films = body.results;
  let result = 0;
  for (let x = 0; x < films.length; x++) {
    const characrter = films[x].characters;
    for (let i = 0; i < characrter.length; i++) {
      if (characrter[i] === 'https://swapi-api.hbtn.io/api/people/18/') {
        result += 1;
      }
    }
  }
  console.log(result);
});
