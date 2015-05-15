#!/usr/bin/python3

import string

space_and_letters = string.ascii_uppercase.upper() + ' \t\n'


def loadDictionary():
    fd = open('dictionary.txt', 'r')
    englishWords = dict()
    for word in fd:
        word = word.strip('\n')
        englishWords[word] = None
    fd.close()
    return(englishWords)


english_words = loadDictionary()



def englishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return(0.0)

    matches = 0
    for word in possibleWords:
        if word in english_words:
            matches += 1
    return(float(matches) / len(possibleWords))



def removeNonLetters(message):
    lettersOnly = list()
    for symbol in message.upper():
        if symbol in space_and_letters:
            lettersOnly.append(symbol)
    return(''.join(lettersOnly))



def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = englishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return(wordsMatch and lettersMatch)
