const fs = require('fs');

function robot(content){
    videoFromPublisher(content)

    function videoFromPublisher(content){
        const videoParams = {
            videoContent: content.sourceContentOriginal,
            videoPublisher: content.sourcePublisher,
            videoAuthors: content.sourceAuthors,
            videoImage: content.sourceUrlToImage
        };
        //console.log(videoParams)    
    }
}

module.exports = robot
