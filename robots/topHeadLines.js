const NewsAPI = require('newsapi');
const NewsAPIKey = require('credentials/googlenews.json').apiKey
var fs = require('fs');
var topHeadlinesFunc = function(){
  newsapi.v2.topHeadlines({
    language: 'en',
    country: 'us'
  }).then(response => {
  var newJson = JSON.stringify(response, null, '\t');// Aqui eu formato json pra ficar mais legível
    //fs.writeFileSync('output.json', newJson);//escrevendo o vetor dentro do arquivo JSON
  });
  return (newJson);
}
module.exports = topHeadlinesFunc;
