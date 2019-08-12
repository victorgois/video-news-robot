const fs = require('fs');
const TextToSpeechV1 = require('ibm-watson/text-to-speech/v1');

function robot(content){
    
    const textToSpeech = new TextToSpeechV1({
        iam_apikey: 'IhF1AMkEvgKFsOfalw9CEFdf5wf_zGXE4nPn01saD3B5',
      });
      
      const synthesizeParams = {
        text: content.sourceDescription,
        accept: 'audio/wav',
        voice: 'pt-BR_IsabelaVoice',
      };
      
      textToSpeech.synthesize(synthesizeParams)
        .then(audio => {
          audio.pipe(fs.createWriteStream('audio.wav'));
        })
        .catch(err => {
          console.log('error:', err);
        });      
}

module.exports = robot
