var Twitter = require('twitter');
 
var client = new Twitter({
  consumer_key: '7a53y0hVHFwUs9Ig0hZ2qKjRP',
  consumer_secret: '2fw76vVXtclWBxukN45XDhpfqdDjSKrbnuXyi5Nsz1mixsKHNA',
  access_token_key: '928002030-RadYSeIbxgGaI2zhvizIqWu0s5cRsK3oe4A0DPZd',
  access_token_secret: 'e8pj2Ht7jK3aMmYsXZfACsz67JTxFpYzeeiB1abvYMNnZ'
});


function start(){

  let content = {}

  let nameArray, volumeArray = []
  
  content.name = getName()
  content.volume = getVolume()

    async function getName() {

      client.get('trends/place', {id : 23424768}, function(error, data, response) {
        if (error) {
          console.log(error);
        }
        var contentFromJson = data[0];
        
        for (var key in contentFromJson.trends){
          nameArray = contentFromJson.trends[key].name + "\n" + nameArray
        }
        console.log(nameArray)
        return(nameArray)
      }
      )};

    async function getVolume() {

      client.get('trends/place', {id : 23424768}, function(error, data, response) {
        if (error) {
          console.log(error);
        }
        var contentFromJson = data[0];

        for (var key in contentFromJson.trends){
          volumeArray = contentFromJson.trends[key].tweet_volume + "\n" + volumeArray
        }
          //console.log(volumeArray)
        return(volumeArray)
      }
      )};

        console.log(content.name)
        console.log(content.volume)
      
    }

  start()
      //console.lo;g(volumes);
    
        //console.log(key, "Name - " + name + ", tweet_vol - " + volume);
  
        /* for (var jey in hashtags){
            hashtags[jey]= jsonResponse.trends[key].name; 
            console.log(hashtags);
          }
          for (var may in volumes){
            volumes[may] = jsonResponse.trends[key].tweet_volume;
          }*/
         // hashtags.forEach((hashtag, i) => result[hashtag] = volume[i]);
  
          //return (result)
  
      //var beforeJson = getNamePair();
      //JSON.stringify(beforeJson);
      //console.log(beforeJson);

