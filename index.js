//var DataFrame = require('dataframe-js').DataFrame;
/*const dataForge = require('data-forge');
const dataForgeWrite = require('data-forge-fs');
*/
var readlineSync = require('readline-sync');
//import sentenceBoundaryDetection from 'sbd';

const robots = {

  everything: require('./robots/text_Everything.js'),
  text: require('./robots/text_topHeadlines.js'),
  //loop: require('./robots/loop.js'),
  //tospeech: require('./robots/toSpeech.js')
  //video: require('./robots/video.js')
}

async function start(){
  
  let content = {}
  
  let contentFromArticles, nameFromArticles, authorsFromArticles, titleFromArticles, descriptionFromArticles, urlfromArticles, urlToImageFromArticles, dateFromArticles, publisherFromArticles = []
  
  content.category = askAndReturnCategory()
  content.query = askandReturnQuery()
  //content.period =  askandReturnPeriod()

  
  //robots.text(content)
  robots.everything(content)

  let contentFromJson = await require('./data/output.json')
  //console.log(dataForge.readFileSync("./output.json"))
  content.sourceContentOriginal = fetchContentFromArticles()
  content.sourcePublisher = fetchNameFromArticles()
  content.sourceAuthors = fetchAuthors()
  content.sourceTitles = fetchTitles()
  content.sourceDescription = fetchDescription()
  content.sourceUrl = fetchUrl()
  content.sourceUrlToImage = fetchUrlToImage()
  content.sourcePublishedAt = fetchDate()
  content.sourcePublisher = fetchPublisher()
  
  //robots.tospeech(content)
  //robots.video(content)

//  downloadImages();


  function askandReturnQuery(){
    
    return readlineSync.question('Digite um termo de busca ou tecle enter para ignorar essa etapa: ')
  }

  function askAndReturnCategory(){
    const prefixes = ["business","entertainment","general","health","science","sports","technology"]
    
    const selectedPrefixIndex = readlineSync.keyInSelect(prefixes,'Escolha uma opcao: ')
    const selectedPrefixText = prefixes[selectedPrefixIndex]

    return (selectedPrefixText)
  }
/*
  function askandReturnPeriod(){
    const period = readlineSync.question('Digite o período que quer buscar: \n')
    return (period)

  }
 */

//Funções de separação de metadados em objetos

  function fetchContentFromArticles(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      contentFromArticles = contentFromJson.articles[i].content + "\n" + contentFromArticles
      //sentences = sentenceBoundaryDetection.sentences(contentFromArticles[i]) + "\n" + sentences
    }
    //console.log(contentFromArticles)
    return(contentFromArticles)
  }

  function fetchNameFromArticles(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      nameFromArticles = contentFromJson.articles[i].source.name + "\n" + nameFromArticles
    }
    //console.log(nameFromArticles)
    return(nameFromArticles)
  }
  
  function fetchAuthors(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      authorsFromArticles = contentFromJson.articles[i].author + "\n" + authorsFromArticles
    }
    //console.log(authorsFromArticles)
    return(authorsFromArticles)
  }

  function fetchTitles(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      titleFromArticles = contentFromJson.articles[i].title + "\n" + titleFromArticles
    }
    //console.log(titleFromArticles)
    return(titleFromArticles)
  }

  function fetchDescription(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      descriptionFromArticles = contentFromJson.articles[i].description + "\n" + descriptionFromArticles
    }
   //console.log(descriptionFromArticles)
    return(descriptionFromArticles)
  }

  function fetchUrl(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      urlfromArticles = contentFromJson.articles[i].url + "\n" + urlfromArticles
    }
    //console.log(urlfromArticles)
    return(urlfromArticles)
  }

  function fetchUrlToImage(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      urlToImageFromArticles = contentFromJson.articles[i].urlToImage + "\n" + urlToImageFromArticles
    }
    //console.log(urlToImageFromArticles)
    return(urlToImageFromArticles)
  }

  function fetchDate(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      dateFromArticles = contentFromJson.articles[i].publishedAt + "\n" + dateFromArticles
    }
    //console.log(dateFromArticles)
    return(dateFromArticles)
  }

  function fetchPublisher(){
    for( var i = 0; i<contentFromJson.articles.source; i++){
      publisherFromArticles = contentFromJson.articles[i].source + "\n" + publisherFromArticles
    }
    //console.log(publisherFromArticles)
    return(publisherFromArticles)
  }
  
  //console.log(content.sourceUrlToImage)
    
    /*setences.forEach((sentence) => {
      content.sentences.push({
        text: sentence,
        keywords: [],
        images: []
      })
    })*/
    //console.log(content.sentences)
  }

start()
