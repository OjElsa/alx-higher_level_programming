#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);

  const fetchAndPrintCharacter = (characterUrl) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        process.exit(1);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  };
  movie.characters.forEach(fetchAndPrintCharacter);
});
