const NewsAPI = require('newsapi');
const newsapi = new NewsAPI('2de5d157d448424db4574be570b492d4');
const readline = require('readline-sync')

var fs = require('fs');

function start(){
  const content = {}

  /*content.category = askAndReturnCategory()
  content.query = askandReturnQuery()*/
  
  function askandReturnQuery(){
    
    const query = readline.question('Digite um termo de busca ou tecle enter para ignorar essa etapa: ')
    return (query)
  }

  function askAndReturnCategory(){
    const prefixes = ["business","entertainment","general","health","science","sports","technology"]
    const selectedPrefixIndex = readline.keyInSelect(prefixes,'Escolha uma opcao: ')
    const selectedPrefixText = prefixes[selectedPrefixIndex]

    return (selectedPrefixText)
  }
  
  newsapi.v2.topHeadlines({
    language: 'pt',
    country: 'br',
    category: askAndReturnCategory(),
    q: askandReturnQuery()
  }).then(response => {
    var newJson = JSON.stringify(response, null, '\t');
    fs.writeFileSync('output.json', newJson);

  });

}


start()
