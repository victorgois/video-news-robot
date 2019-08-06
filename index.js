
const readline = require('readline-sync')

const robots = {
  //userInput: require('./robots/user-input.js')
  text: require('./robots/text.js')
}

async function start(){
  const content = {}

  content.category = askAndReturnCategory()
  content.query = askandReturnQuery()

  //robots.userInput(content)
  await robots.text(content)
  
  function askandReturnQuery(){
    
    return readline.question('Digite um termo de busca ou tecle enter para ignorar essa etapa: ')
  }

  function askAndReturnCategory(){
    const prefixes = ["business","entertainment","general","health","science","sports","technology"]
    const selectedPrefixIndex = readline.keyInSelect(prefixes,'Escolha uma opcao: ')
    const selectedPrefixText = prefixes[selectedPrefixIndex]

    return (selectedPrefixText)
  }

}

start()
