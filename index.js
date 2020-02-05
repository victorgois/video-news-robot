//var DataFrame = require('dataframe-js').DataFrame;
/*const dataForge = require('data-forge');
const dataForgeWrite = require('data-forge-fs');
*/
var readlineSync = require('readline-sync');
const fs = require('fs');  
  request = require('request');

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
  
  let contentFromArticles = []
  let dateFromArticles = []
  let nameFromArticles = []
  let authorsFromArticles = []
  let titleFromArticles = []
  let descriptionFromArticles = []
  let urlfromArticles = []
  let urlToImageFromArticles = []
  let publisherFromArticles = []
  
  //content.category = askAndReturnCategory()
  //content.query = askandReturnQuery()
  //content.query = '+tecnologia AND (uber AND aplicativo) OR (cripto) OR (ciber) OR (vigilância AND dados) OR  (dados AND direitos) OR (dados AND capitalismo) OR (hacker) OR (metadados) OR (algoritmo AND dados) OR (big data) OR (deep fake) OR (transhumanismo) OR (ficção científica) OR (machine learning) OR (aprendizado de máquina) OR (inteligência artificial) OR (dados AND coleta) OR (digital AND filosofia) OR (fake news)'
  //content.period =  askandReturnPeriod()

  
  //robots.text(content)
  robots.everything(content)

  let contentFromJson = await require('./data/output.json')
  //console.log(dataForge.readFileSync("./output.json"))
  content.sourceContentOriginal = fetchContentFromArticles()
  content.sourceName = fetchNameFromArticles()
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
      contentFromArticles.push(contentFromJson.articles[i].content)
      //sentences = sentenceBoundaryDetection.sentences(contentFromArticles[i]) + "\n" + sentences
    }
    //console.log(contentFromArticles)
    return(contentFromArticles)
  }

  function fetchNameFromArticles(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      nameFromArticles.push(contentFromJson.articles[i].source.name)
    }
    //console.log(nameFromArticles)
    return(nameFromArticles)
  }
  
  function fetchAuthors(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      authorsFromArticles.push(contentFromJson.articles[i].author)
    }
    //console.log(authorsFromArticles)
    return(authorsFromArticles)
  }

  function fetchTitles(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      titleFromArticles.push(contentFromJson.articles[i].title)
    }
    //console.log(titleFromArticles)
    return(titleFromArticles)
  }

  function fetchDescription(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      descriptionFromArticles.push(contentFromJson.articles[i].description)
    }
   //console.log(descriptionFromArticles)
    return(descriptionFromArticles)
  }

  function fetchUrl(){
    for( var i = 0; i<contentFromJson.articles.length; i++){
      urlfromArticles.push(contentFromJson.articles[i].url)
    }
    //console.log(urlfromArticles)
    return(urlfromArticles)
  }

  function fetchUrlToImage(){
    var download = function(uri, filename, callback){
      request.head(uri, function(err, res, body){
        request(uri).pipe(fs.createWriteStream(filename)).on('close', callback);
      });
    };

    for( var i = 0; i<contentFromJson.articles.length; i++){
      urlToImageFromArticles.push(contentFromJson.articles[i].urlToImage)
    }
    for( var i = 0; i<urlToImageFromArticles.length; i++){
      download(urlToImageFromArticles[i], './images/image'+ i +'.png', function(){
        console.log('malfeito, feito');
    })
    }

    return(urlToImageFromArticles)
  }

  function fetchDate(){
    //Convert the date to human readeable
    function formatDate(stringDate){
      var date=new Date(stringDate);
      return date.getDate() + '/' + (date.getMonth() + 1) + '/' +  date.getFullYear();
    }
    for( var i = 0; i<contentFromJson.articles.length; i++){
      dateFromArticles.push(formatDate(contentFromJson.articles[i].publishedAt))
    }

    return(dateFromArticles)
  }

  function fetchPublisher(){
    for( var i = 0; i<contentFromJson.articles.source; i++){
      publisherFromArticles.push(contentFromJson.articles[i].source)
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
