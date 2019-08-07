
const readline = require('readline-sync')

const robots = {
  //userInput: require('./robots/user-input.js')
  text: require('./robots/text.js')
}

function start(){
  const content = {}

  content.category = askAndReturnCategory()
  content.query = askandReturnQuery()
  robots.text(content)
  const contentFromJson = require('./output.json')
  content.sourceContentOriginal = fetchContentFromArticles()
  content.sourcePublisher = fetchNameFromArticles()
  /*content.souceAuthors =
  content.sourceTitles =
  content.sourceDescription = 
  content.souceUrl = 
  content.sourceUrlToImage = 
  content.sourcePublishedAt = 
  */
  //robots.userInput(content)
  
  function askandReturnQuery(){
    
    return readline.question('Digite um termo de busca ou tecle enter para ignorar essa etapa: ')
  }

  function askAndReturnCategory(){
    const prefixes = ["business","entertainment","general","health","science","sports","technology"]
    const selectedPrefixIndex = readline.keyInSelect(prefixes,'Escolha uma opcao: ')
    const selectedPrefixText = prefixes[selectedPrefixIndex]

    return (selectedPrefixText)
  }

  function fetchContentFromArticles(){
    for( var i = 0; i<contentFromJson.totalResults; i++){
      const contentFromArticles = contentFromJson.articles[i].content
      console.log(contentFromArticles)
    }
    return(contentFromArticles)
  }
  function fetchNameFromArticles(){
    for( var i = 0; i<contentFromJson.totalResults; i++){
      const nameFromArticles = contentFromJson.articles[i].source.name
      console.log(nameFromArticles)
    }
    return(nameFromArticles)
  }  
}

start()
