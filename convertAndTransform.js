const fs = require('fs');
    request = require('request');

let publishedAtArray = []
let imageUrlArray = []
let convertedDate = []

function formatDate(stringDate){
    var date=new Date(stringDate);
    return date.getDate() + '/' + (date.getMonth() + 1) + '/' +  date.getFullYear();
}

let rawdata = fs.readFileSync('./data/output.json');
let jsondata = JSON.parse(rawdata)

for (var i = 0; i<jsondata.articles.length; i++){
    publishedAtArray.push(jsondata.articles[i].publishedAt)
    imageUrlArray.push(jsondata.articles[i].urlToImage)
}

for (var i = 0; i<publishedAtArray.length; i++){
    convertedDate.push(formatDate(publishedAtArray[i]))
}

var download = function(uri, filename, callback){
    request.head(uri, function(err, res, body){
      request(uri).pipe(fs.createWriteStream(filename)).on('close', callback);
    });
  };

for (var i = 0; i<imageUrlArray.length; i++){
    download(imageUrlArray[i], './images/image'+ i +'.png', function(){
        console.log('malfeito, feito');
    })
};