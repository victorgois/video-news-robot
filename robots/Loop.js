
var loopDiarioFunc = function loopDiario(newJson){
    var BaseDados = [];
    BaseDados = newJson;//vetor de JSON
    fs.writeFileSync('output.json', BaseDados);
}
module.exports = robot;
