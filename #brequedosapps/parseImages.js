const fs = require('fs');
request = require('request');

let rawdatanews = fs.readFileSync('./news.json');
let rawdatatweets = fs.readFileSync('./tweets.json');

let news = JSON.parse(rawdatanews);
let tweets = JSON.parse(rawdatatweets);

const tweetsParse = (source) => {

    //Downloading the images from the news
    let download = function(uri, filename, callback){
        request.head(uri, function(err, res, body){
        console.log('content-type:', res.headers['content-type']);
        console.log('content-length:', res.headers['content-length']);
    
        request(uri).pipe(fs.createWriteStream('./images/tweets/'+filename)).on('close', callback);
        });
    };

    size = source.length;

    for( i=0; i<size; i++ ){
        img = source[i]['img_urls'];
        console.log(img)
        if (typeof img[0] !== 'undefined') {
            download(img[0], 'image' + i + '.png',function(){
                console.log('done');
            })        
        }

    }
}

const newsParse = (source) => {

    //Downloading the images from the news
    let download = function(uri, filename, callback){
        request.head(uri, function(err, res, body){
        console.log('content-type:', res.headers['content-type']);
        console.log('content-length:', res.headers['content-length']);
    
        request(uri).pipe(fs.createWriteStream('./images/'+filename)).on('close', callback);
        });
    };

    size = source['articles'].length;
    articles = source['articles'];

    for( i=0; i<size; i++ ){
        download(articles[i]['urlToImage'], 'image' + i + '.png',function(){
            console.log('done');
        })
    }
}

tweetsParse(tweets);



