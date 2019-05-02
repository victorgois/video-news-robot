module.exports = {

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
