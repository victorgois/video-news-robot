const NewsAPI = require('newsapi');
//const googleNewsapiKey = require('../credentials/googlenews.json').apiKey;

const newsapiKey = new NewsAPI('2de5d157d448424db4574be570b492d4');

var fs = require('fs');
//var readlineSync = require('readline-sync');

async function robot(content){
  await fetchContentFromGoogleNews(content)
  //sanitizeContent(content)
  //breakContentIntoSentences(content)

  async function fetchContentFromGoogleNews(content){
    newsapiKey.v2.everything({
    language: 'pt',
    //category: content.category,
    //q: content.query,
    q: ' (uber AND aplicativo) OR  (dados AND informação AND política AND direitos) OR (dados AND capitalismo) OR (hacker) OR (dados AND metadados) OR (algoritmo AND dados) OR (deep fake) OR (transhumanismo) OR (ficção científica AND tecnologia) OR (inteligência artificial AND aprendizado de máquina) OR (dados AND fake news) OR (digital AND filosofia) OR (design AND cultura maker)',
    from: '2020-01-28', //return readlineSync.question('Digite um termo de busca ou tecle enter para ignorar essa etapa: ')
    to: '2020-01-31',
    sortBy: 'relevancy',
    pagesize: '100'
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

 
}
    module.exports = robot
