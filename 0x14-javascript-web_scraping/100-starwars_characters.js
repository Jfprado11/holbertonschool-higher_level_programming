#!/usr/bin/node

const url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];

const request = require("request");
request.get({ url: url, json: true }, function (error, r, body) {
  if (error) {
    console.error(error);
  }
  const characters = body.characters;
  for (const character of characters) {
    request.get({ url: character, json: true }, (err, res, info) => {
      if (err) {
        console.error(err);
      }
      console.log(info.name);
    });
  }
});
