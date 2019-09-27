const NewsAPI = require('newsapi');
const newsapiKey = new NewsAPI('2de5d157d448424db4574be570b492d4');
var fs = require('fs');
//var readlineSync = require('readline-sync');

function robot(content){
  fetchContentFromGoogleNews(content)
  //sanitizeContent(content)
  //breakContentIntoSentences(content)

  async function fetchContentFromGoogleNews(content){
    newsapiKey.v2.everything({
    language: 'pt',
    //category: content.category,
    q: content.query,
    from: '2019-09-20', //return readlineSync.question('Digite um termo de busca ou tecle enter para ignorar essa etapa: ')
    to: '2019-09-26',
    sortBy: 'relevance',
    page: 10,
  }).then(response => {
    const newJson = JSON.stringify(response, null, '\t');
    /*
    if (content.category == '1'){
      fs.writeFileSync('./data/business/output.json', newJson);
      const contentFromJson = JSON.parse(newJson)
    }*/
    fs.writeFileSync('./data/output.json', newJson);
    const contentFromJson = JSON.parse(newJson)
    //console.log(contentFromJson)
    return(contentFromJson)
  });
  }

  /*function sanitizeContent(content){
    const withoutBlanklines = removeBlanklines(content.sourceDescription)
    console.log(withoutBlanklines)

      function removeBlanklines(text){
        const alllines = text.split('\n')

        const withoutBlanklines = alllines.filter((line)=> {
          if (line.trim().length === 0) {
            return false
          }
          return true
        })
        return withoutBlanklines
      }
  }
  */
}
    module.exports = robot

      /*const authorFromArticles = contentFromJson.articles[i].author
      const titleFromArticles = contentFromJson.articles[i].title
      const descriptionFromArticles = contentFromJson.articles[i].description
      const urlFromArticles = contentFromJson.articles[i].url
      const urlToImagefromArticles = contentFromJson.articles[i].urlToImage
      const dateFromArticles = contentFromJson.articles[i].publishedAt */
    
    //console.log(content.sourcePublishedAt)


  //return(content.sourceContentOriginal)


  /*function sanitizeContent(content){
    console.log(sourceContentOriginal)
    const withoutBlankLines = removeBlanklines(content.sourceContentOriginal)

    function removeBlanklines(text){
      const allLines = text.split('\n')
      console.log(allLines)
    }
  }
}*/



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