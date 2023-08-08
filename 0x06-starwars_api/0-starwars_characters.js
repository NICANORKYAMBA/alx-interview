#!/usr/bin/node
const request = require('request');

function fetchMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('API responded with status code:', response.statusCode);
      return;
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    fetchStarWarsCharacters(characterUrls);
  });
}

function fetchStarWarsCharacters (characterUrls) {
  const characterPromises = characterUrls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          reject(new Error(`API responded with status code: ${response.statusCode}`));
          return;
        }

        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => {
        console.log(name);
      });
    })
    .catch(error => {
      console.error('Error fetching character data:', error);
    });
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID!');
} else {
  fetchMovieCharacters(movieId);
}
