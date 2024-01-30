#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    return;
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  charactersUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
