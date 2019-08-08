const NewsAPI = require('newsapi');
const newsapiKey = new NewsAPI('2de5d157d448424db4574be570b492d4');
var fs = require('fs');

function robot(content){
  fetchContentFromGoogleNews(content)
  parseContentFromGoogleNews('./output.json')
  //parsePublisherFromGoogleNews(content)
  //parseAuthorsFromGoogleNews(content)
  //parseTitlesFromGoogleNews(content)
  //parseDescriptionFromGoogleNews(content)
  //parseUrlFromGoogleNews(content)
  //parseUrlToImageFromGoogleNews(content)
  //parsePublishAtGoogleNews(content)
  //console.log(fetchContentFromGoogleNews())
  //sanitizeContent(content)
  //breakContentIntoSentences(content)

   function fetchContentFromGoogleNews(content){
    newsapiKey.v2.topHeadlines({
    language: 'pt',
    country: 'br',
    category: content.category,
    q: content.query
  }).then(response => {
    const newJson = JSON.stringify(response, null, '\t');
    fs.writeFileSync('output.json', newJson);
    //const contentFromJson = JSON.parse(newJson)
    //console.log(contentFromJson)
    //console.log(content.sourcePublishedAt)

  });
  //return(content.sourceContentOriginal)
  }

  function parseContentFromGoogleNews(content){
    for( var i = 0; i<content.totalResults; i++){
      const contentFromJson = content.articles[i].content
    }
  }

  /* content.sourcePublisher = contentFromJson.articles[i].source.name
      content.souceAuthors = contentFromJson.articles[i].author
      content.sourceTitles = contentFromJson.articles[i].title
      content.sourceDescription = contentFromJson.articles[i].description
      content.souceUrl = contentFromJson.articles[i].url
      content.sourceUrlToImage = contentFromJson.articles[i].urlToImage
      content.sourcePublishedAt = contentFromJson.articles[i].publishedAt */

  function sanitizeContent(content){
    console.log(sourceContentOriginal)
    const withoutBlankLines = removeBlanklines(content.sourceContentOriginal)

    function removeBlanklines(text){
      const allLines = text.split('\n')
      console.log(allLines)
    }
  }
}

module.exports = robot


/*module.exports = {  

   authorsFunction: function (){
    const fs = require('fs');
    let rawdata = fs.readFileSync('../data/output.json');
    let output = JSON.parse(rawdata);
    var arr = [];
    //for (var i=0; i<output.totalResults; i++){
      //arr = (output.articles[i].author);
      //console.log(arr);
    //}
    output.articles.forEach(function (item){
      arr = item.author;
      //console.log(arr);
      return (arr);
    })
  },

  titleFunction: function (){
  const fs = require('fs');
  let rawdata = fs.readFileSync('../data/output.json');
  let output = JSON.parse(rawdata);
  var arr = [];
  output.articles.forEach(function (item){
    arr = item.title;
    //console.log(arr);
    return (arr);
  })
},
  descriptionFunction: function (){
    const fs = require('fs');
    let rawdata = fs.readFileSync('../data/output.json');
    let output = JSON.parse(rawdata);
    var arr = [];
    output.articles.forEach(function (item){
      arr = item.description;
      //console.log(arr);
      return (arr);
    })
  },
  publishedAtFunction: function(){
    const fs = require('fs');
    let rawdata = fs.readFileSync('../data/output.json');
    let output = JSON.parse(rawdata);
    var arr = [];
    output.articles.forEach(function (item){
      arr = item.publishedAt;
      //console.log(arr);
      return (arr);
    })
  },
  urlToImageFunction: function(){
    const fs = require('fs');
    let rawdata = fs.readFileSync('../data/output.json');
    let output = JSON.parse(rawdata);
    var arr = [];
    output.articles.forEach(function (item){
      arr = item.urlToImage;
      //console.log(arr);
      return (arr);
    })
  }
}
*/