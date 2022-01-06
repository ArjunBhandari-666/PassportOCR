const tesseract = require("tesseract.js")
const fs = require("fs")

tesseract.recognize("image-text.jpg", "eng", {
    logger: m => console.log(m)
}).then(result => {
    console.log(result.data.text)
}).catch(err => {
})

const getImageText = async (fileName, lang, logger) => {
    let recognizeResult = null
    try {
        if (fs.existsSync(fileName)) {
            if (logger) {
                const myLogger = {
                    logger: m => console.log(m)
                }
                recognizeResult = await tesseract.recognize(fileName, lang, myLogger)
            } else {
                recognizeResult = await tesseract.recognize(fileName, lang)
            }
            if (recognizeResult) {
                return recognizeResult.data.text
            }
        }
    } catch (error) {
        return error.message
    }
}

// getImageText("image-text.jpg", "eng", false).then(text => {
//     console.log(text)
// }).catch(errMsg => {
//     console.log(errMsg)
// })