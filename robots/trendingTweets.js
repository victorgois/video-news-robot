var https = require('https');
var headers = {
  'User-Agent': 'Coding Defined',
  Authorization: 'bearer ' + require('./oauth.json').access_token
};

function jsonHandler(response, callback) {
    var json = '';
    response.setEncoding('utf8');
    if(response.statusCode === 200) {
      response.on('data', function(chunk) {
        json += chunk;
      }).on('end', function() {
        callback(JSON.parse(json));
      });
    } else {
      console.log('Error : ' + reseponse.statusCode);
    }
  }

  var trendOptions = {
    host: 'api.twitter.com',
    path: '/1.1/trends/place.json?id=1', // id = 1 for global trends
    headers: headers
  }
  
  var tweetDetails = {
    maxresults: 10,
    resultType: 'recent', // options are mixed, popular and recent
    options: {
      host: 'api.twitter.com',
      headers: headers,
    }
  }

  function fullTweetPath(query) {
    var path = '/1.1/search/tweets.json?q=' + query
    + '&count=' + tweetDetails.maxResult
    + '&include_entities=true&result_type=' + tweetDetails.resultType;
  
    tweetDetails.options.path = path; 
  }

  function callTwitter(options, callback){
    https.get(options, function(response) {
      jsonHandler(response, callback);
    }).on('error', function(e) {
      console.log('Error : ' + e.message);
    })
  }