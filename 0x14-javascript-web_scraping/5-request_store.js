#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const filmurl = process.argv[2];
const filmfile = process.argv[3];

request
  .get(filmurl, (err, response, body) => {
    if (err) console.log(err);
    else if (body) {
      fs.writeFile(filmfile, body, 'utf-8', function (err) {
        if (err) console.log(err);
      });
    }
  });
