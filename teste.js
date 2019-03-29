const NewsAPI = require('newsapi');
const newsapi = new NewsAPI('2de5d157d448424db4574be570b492d4');
var fs = require('fs');

// To query top headlines
// All options passed to topHeadlines are optional, but you need to include at least one of them
newsapi.v2.topHeadlines({
  language: 'pt',
  country: 'br'
}).then(response => {
  let data = JSON.stringify(response);
  fs.writeFileSync('output.json', data);
    
  //console.log(response);
  /*
    {
      status: "ok",
      articles: [...]
    }
  */
});

