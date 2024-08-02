#!/usr/bin/node

const request = require('request');
const filmid = process.argv[2];

request
  .get(`https://swapi-api.alx-tools.com/api/films/${filmid}`, (err, response, body) => {
    if (err) console.log(err);
    else if (body) {
      const responsebody = JSON.parse(body);
      const chart = responsebody.characters;
      for (const i of chart) {
        request.get(i, (error, res, body1) => {
          if (error) {
            console.log(error);
          }
          const data1 = JSON.parse(body1);
          console.log(data1.name);
        });
      }
    }
  });
