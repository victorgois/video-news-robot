const fs = require('fs');
const TextToSpeechV1 = require('ibm-watson/text-to-speech/v1');

function robot(content){
  fetchAudioFromIBM(content)

  function fetchAudioFromIBM(content){
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
      //var audio = [];
      //for (i = 0; i<content.articles.length; i++){
        //audio[i] = new Audio()
        //audio[i].src = audio.pipe(fs.createWriteStream('./audios/audioPublisher.wav')); //testando a criação de loop na produção do áudio
  audio.pipe(fs.createWriteStream('./audios/audioPublisher.wav')); //testando a criação de loop na produção do áudio
      //audio[i].play();
    })
    .catch(err => {
      console.log('error:', err);
    });      
  }
} 

module.exports = robot
