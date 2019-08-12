
const readline = require('readline-sync')

const robots = {
  //userInput: require('./robots/user-input.js')
  text: require('./robots/text.js'),
  //loop: require('./robots/loop.js'),
  tospeech: require('./robots/toSpeech.js')
  //video: require('./robots/video.js')
}

function start(){
  let content = {}
  
  let contentFromArticles, nameFromArticles, authorsFromArticles, titleFromArticles, descriptionFromArticles, urlfromArticles, urlToImageFromArticles, dateFromArticles = []
  
  content.category = askAndReturnCategory()
  content.query = askandReturnQuery()
  
  robots.text(content)
  let contentFromJson = require('./output.json')
  
  content.sourceContentOriginal = fetchContentFromArticles()
  content.sourcePublisher = fetchNameFromArticles()
  content.souceAuthors = fetchAuthors()
  content.sourceTitles = fetchTitles()
  content.sourceDescription = fetchDescription()
  content.souceUrl = fetchUrl()
  content.sourceUrlToImage = fetchUrlToImage()
  content.sourcePublishedAt = fetchDate()
  
  robots.tospeech(content)
  //robots.loop(content)

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
    for( var i = 0; i<contentFromJson.articles.length; i++){
      contentFromArticles = contentFromJson.articles[i].content
      //console.log(contentFromArticles)
    }
    return(contentFromArticles)
  }

  function fetchNameFromArticles(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      nameFromArticles = contentFromJson.articles[i].source.name
      //console.log(nameFromArticles)
    }
    return(nameFromArticles)
  }
  
  function fetchAuthors(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      authorsFromArticles = contentFromJson.articles[i].author
    //console.log(authorsFromArticles)
    }
    return(authorsFromArticles)
  }

  function fetchTitles(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      titleFromArticles = contentFromJson.articles[i].title
      //console.log(titleFromArticles)
    }
    return(titleFromArticles)
  }

  function fetchDescription(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      descriptionFromArticles = contentFromJson.articles[i].description
      //console.log(descriptionFromArticles)
    }
    return(descriptionFromArticles)
  }

  function fetchUrl(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      urlfromArticles = contentFromJson.articles[i].url
      //console.log(urlfromArticles)
    }
    return(urlfromArticles)
  }

  function fetchUrlToImage(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      urlToImageFromArticles = contentFromJson.articles[i].urlToImage
      //console.log(urlToImageFromArticles)
    }
    return(urlToImageFromArticles)
  }

  function fetchDate(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      dateFromArticles = contentFromJson.articles[i].publishedAt
      //console.log(dateFromArticles)
    }
    return(dateFromArticles)
  }
}

start()
