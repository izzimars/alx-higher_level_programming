#!/usr/bin/node

const request = require('request');
const filmurl = process.argv[2];

request
  .get(filmurl, (err, response, body) => {
    if (err) console.log(err);
    else if (body) {
      const responsebody = JSON.parse(body);
      const result = responsebody.results;
      let count = 0;
      for (let i = 0; i < result.length; i++) {
        const charid = 'https://swapi-api.alx-tools.com/api/people/18/';
        if (result[i].characters.includes(charid)) count += 1;
      }
      console.log(count);
    }
  });
