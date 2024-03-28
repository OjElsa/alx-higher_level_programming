#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);
  movie.characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
