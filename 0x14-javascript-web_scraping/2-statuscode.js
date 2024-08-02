#!/usr/bin/node

const request = require('request');
const fileurl = process.argv[2];

request
  .get(fileurl)
  .on('response', function (response) {
    console.log(response.statusCode);
  });
