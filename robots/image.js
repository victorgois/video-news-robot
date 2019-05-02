
//var newJsonFunc = require('topHeadlines');

var urlImagesFunc = async function urlToImage(){
  app.locals.output = require('./output.json'); //substituir por newsJsonFunc na implementação Final
  output.articles.forEach(function(item){
    var urlImages = item.urlToImage;
return (urlImages);
  })
return (urlImagesFunc)
console.log(urlToImage);
}
module.exports = robot;
