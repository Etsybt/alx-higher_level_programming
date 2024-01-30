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

  const fetchCharacter = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          reject();
          return;
        }

        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  };

  Promise.all(charactersUrls.map(fetchCharacter))
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(() => {

    });
});
