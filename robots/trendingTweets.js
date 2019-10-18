var Twitter = require('twitter');
 
var client = new Twitter({
  consumer_key: '7a53y0hVHFwUs9Ig0hZ2qKjRP',
  consumer_secret: '2fw76vVXtclWBxukN45XDhpfqdDjSKrbnuXyi5Nsz1mixsKHNA',
  access_token_key: '928002030-RadYSeIbxgGaI2zhvizIqWu0s5cRsK3oe4A0DPZd',
  access_token_secret: 'e8pj2Ht7jK3aMmYsXZfACsz67JTxFpYzeeiB1abvYMNnZ'
});
 
client.get('trends/place', {id : 23424768}, function(error, data, response) {
  if (error) {
    console.log(error);
    }
    var jsonResponse = data[0];
    let hashtags, volumes = [];
    function getNamePair(hashtags, volumes) {
      for (var key in jsonResponse.trends) {
        for (var jey in hashtags){
          hashtags[jey]= jsonResponse.trends[key].name; 
          console.log(hashtags);
        }
        for (var may in volumes){
          volumes[may] = jsonResponse.trends[key].tweet_volume;
        }
        var result = {};
        hashtags.forEach((hashtag, i) => result[hashtag] = volume[i]);

        }
        //console.log(key, "Name - " + name + ", tweet_vol - " + volume);
        return (result)
    }
    var beforeJson = getNamePair();
    JSON.stringify(beforeJson);
    console.log(beforeJson);
});