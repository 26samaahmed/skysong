// const { error } = require('console');
const request = require('request')

require('dotenv').config()

// Send an Authorization Request. I am using the Client Credentials Flow Authorization

var CLIENT_ID=process.env.SPOTIFY_CLIENT_ID;
//console.log(`Client ID is: ${SPOTIFY_CLIENT_ID}`);
var CLIENT_SECRET=process.env.SPOTIFY_CLIENT_SECRET;
//console.log(`Client Secret is: ${SPOTIFY_CLIENT_SECRET}`);

var authorizationOptions = {
  url: 'https://accounts.spotify.com/api/token',
  headers: {
    'Authorization': 'Basic ' + (new Buffer.from(CLIENT_ID + ':' + CLIENT_SECRET).toString('base64'))
  },
  form: {
    grant_type: 'client credentials'
  },
  json: true
};

request.post(authorizationOptions, function(error, response, body) {
  if (!error && response.statusCode === 200) {
    var token = body.access_token;
  } else {
    console.log(error);
  }
});

