/**
 * @description reverses a string 
 * @param {String} word 
 * @returns {String} newWord 
 */
const reverseString = word => {
    const stringLength = word.length 
    let loopCount = 0 
    let newWord = ""
    while(loopCount < stringLength){
        newWord = newWord + word[stringLength - 1 - loopCount]
        loopCount += 1
    }
    return newWord
}

const test = reverseString("Cat") 
console.log(test)