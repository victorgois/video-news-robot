const NewsAPI = require('newsapi');
//const NewsAPIKey = require('../credentials/googlenews.json').apiKey
const NewsAPIKey = new NewsAPI('2de5d157d448424db4574be570b492d4');
var fs = require('fs');
NewsAPIKey.v2.topHeadlines({
  category: 'politics',
  language: 'pt',
  country: 'br'
  }).then(response => {
    var newJson = JSON.stringify(response, null, '\t');// Aqui eu formato json pra ficar mais legível
    fs.writeFileSync('../data/output.json', newJson);//escrevendo o vetor dentro do arquivo JSON
    //console.log(newJson);
  });

//module.exports = newJson;
