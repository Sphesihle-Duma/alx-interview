#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line argument
const movieId = process.argv[2];

// Make a GET request to the Star Wars API films endpoint
request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else if (response.statusCode !== 200) {
        console.error('Status:', response.statusCode);
    } else {
        const filmData = JSON.parse(body);
        const charactersUrls = filmData.characters;
        
        // Array to store character names
        const characters = [];

        // Function to fetch character names recursively
        const fetchCharacterNames = (urls, index) => {
            if (index === urls.length) {
                // All character names fetched, print them
                characters.forEach(character => console.log(character));
                return;
            }
            request(urls[index], (error, response, body) => {
                if (error) {
                    console.error('Error:', error);
                } else if (response.statusCode !== 200) {
                    console.error('Status:', response.statusCode);
                } else {
                    const characterData = JSON.parse(body);
                    characters.push(characterData.name);
                    // Fetch next character name
                    fetchCharacterNames(urls, index + 1);
                }
            });
        };

        // Start fetching character names
        fetchCharacterNames(charactersUrls, 0);
    }
});

