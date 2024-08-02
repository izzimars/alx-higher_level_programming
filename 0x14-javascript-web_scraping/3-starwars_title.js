#!/usr/bin/node

const request = require('request');
const filmid = process.argv[2];

request
  .get(`https://swapi-api.alx-tools.com/api/films/${filmid}`, (err, response, body) => {
    if (err) console.log(err);
    else if (body) {
      const responsebody = JSON.parse(body);
      console.log(responsebody.title);
    }
  });
