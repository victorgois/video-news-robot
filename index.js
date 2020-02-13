//var DataFrame = require('dataframe-js').DataFrame;
/*const dataForge = require('data-forge');
const dataForgeWrite = require('data-forge-fs');
*/
var readlineSync = require('readline-sync');
var json = require('json-update');
const fs = require('fs');  
  request = require('request');

//import sentenceBoundaryDetection from 'sbd';

const robots = {

  everything: require('./robots/text_Everything.js'),
  //headlines: require('./robots/text_topHeadlines.js'),
  sanitize: require('./robots/sanitize.js')
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
  
  //robots.headlines(content)
  await robots.everything(content)

  let contentFromJson = require('./data/output.json')
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
  

  robots.sanitize(content)
  //robots.tospeech(content)
  //robots.video(content)

//  downloadImages();

//console.log(content.sourceDescription)

//FUNCTIONS

  function askandReturnQuery(){
    
    return readlineSync.question('Digite um termo de busca ou tecle enter para ignorar essa etapa: ')
  }

  function askAndReturnCategory(){
    const prefixes = ["business","entertainment","general","health","science","sports","technology"]
    
    const selectedPrefixIndex = readlineSync.keyInSelect(prefixes,'Escolha uma opcao: ')
    const selectedPrefixText = prefixes[selectedPrefixIndex]

    return (selectedPrefixText)
  }

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
      var alphabetLetters = /^[A-Za-z]+$/
      if ((contentFromJson.articles[i].description.length < 250) || (contentFromJson.articles[i].description.endsWith('...') == false)  || (contentFromJson.articles[i].description.endsWith('... Leia mais') == false) || (contentFromJson.articles[i].description.endsWith(alphabetLetters) == false)){
        descriptionFromArticles.push(contentFromJson.articles[i].description)
        //console.log(i)
      }
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
    })
    }

    return(urlToImageFromArticles)
  }

  function fetchDate(){
    //Convert the date to human readeable

    function formatDate(stringDate) {
      var date = new Date(stringDate);
      return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear();
    }
    for( var i = 0; i<contentFromJson.articles.length; i++){
      dateFromArticles.push(formatDate(contentFromJson.articles[i].publishedAt))
    }

    json.load('./data/output.json', function(err,obj){
      for (var i = 0; i<obj.articles.length; i++){
        const values = Object.entries(obj.articles[i])
        for (const [key,value] of values){
          var j = 0;
          if (key == 'publishedAt'){
            original = dateFromArticles[j]
            //console.log(original)

            async function test() {
              await update('./data/output.json', {'publishedAt': original[j]});
              j+=1
              let dat = await load('./data/output.json');
              console.log(dat.publishedAt);
            }
             
            test().then(()=> {}).catch( e=> {console.error(e)}); 

/*             json.update('./data/output.json',{'publishedAt': original[j]})
            .then(function(dat) { 
              console.log(dat.publishedAt) 
            }); */
          }
        }
      }
    })

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
