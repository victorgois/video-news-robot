let contentFromJson = require('./data/output.json')

for( var i = 0; i<contentFromJson.articles.length; i++){
    console.log(contentFromJson.articles[i].source.name)
}