#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movie ID>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
