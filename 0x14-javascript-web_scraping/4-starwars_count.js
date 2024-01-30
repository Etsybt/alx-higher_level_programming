#!/usr/bin/node

const request = require('request');
const starWarsApiUrl = process.argv[2];
let appearanceCount = 0;

request(starWarsApiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
    return;
  }

  const films = JSON.parse(body).results;

  for (let i = 0; i < films.length; ++i) {
    const characters = films[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const characterUrl = characters[j];
      const characterId = characterUrl.split('/')[5];

      if (characterId === '18') {
        appearanceCount += 1;
      }
    }
  }

  console.log(appearanceCount);
});
