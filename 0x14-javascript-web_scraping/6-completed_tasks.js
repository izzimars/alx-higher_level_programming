#!/usr/bin/node

const request = require('request');
const filmurl = process.argv[2];

request
  .get(filmurl, (err, response, body) => {
    if (err) console.log(err);
    else if (body) {
      const resbody = JSON.parse(body);
      const arr = {};
      for (let i = 0; i < resbody.length; i++) {
        if (resbody[i].completed) {
          if (resbody[i].userId in arr) {
            arr[resbody[i].userId] = arr[resbody[i].userId] + 1;
          } else {
            arr[resbody[i].userId] = 1;
          }
        }
      }
      console.log(arr);
    }
  });
