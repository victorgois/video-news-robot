
//app.locals.output = require('../data/output.json');
const robots = {
  googlenews: require('./robots/input.js'),
  text: require('./robots/text.js'),
  //loop: require('./robots/loop.js'),
  //image: require('./robots/image.js'),
  //video: require('./robots/video.js'),
  //youtube: require('./robots/youtube.js')
}

async function start() {
  robots.googlenews()
  await robots.text()
  //await robots.image()
  //await robots.video()
  //await robots.youtube()
}

start()

var text = require('./text');
//text.authorsFunction();
var textTitle = [];
textTitle = text.titleFunction();
var textDescription = [];
textDescription = text.descriptionFunction();
var textPublished = [];
textPublished = text.publishedAtFunction();
var textUrlImage = [];
textUrlImage = text.urlToImageFunction();

console.log(textTitle);


//setTimeout(topHeadlines,86400000) // Executa a função topHeadlines a cada 24h
