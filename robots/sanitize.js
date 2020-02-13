function robot(content){
    sanitizeContent(content)


    function sanitizeContent(content){
        const withoutBlanklines = removeBlanklines(content.sourceDescription)
        //console.log(withoutBlanklines)

        function removeBlanklines(text){
            text = text + ''
            const alllines = text.split('\n')

            const withoutBlanklines = alllines.filter((line) => {
            if (line.trim().length === 0) {
                return false
            }
            return true
            })
            return withoutBlanklines
        }
    }

}

module.exports = robot
