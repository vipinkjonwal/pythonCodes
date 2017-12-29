def splitSentence(sentence):
    indexList = []
    wordsList = []
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            indexList.append(i)

    i = 0
    j = 0
    for i in indexList:
        wordsList.append(sentence[j:i])
        j = i+1
    wordsList.append(sentence[j:len(sentence)])

    return wordsList

def reverseSentence(sentence):
    i = 0
    j = len(sentence) - 1

    while i < j:
        sentence[i],sentence[j] = sentence[j],sentence[i]
        i += 1
        j -= 1

    return sentence

def joinSentence(sentence):
    finalSentence = ''

    for i in sentence:
        finalSentence += i
        finalSentence += ' '

    return finalSentence

def main():
    sentence = 'I have successfully programmed this problem'
    print('Given Sentence:',sentence)
    wordsList = splitSentence(sentence)
    reverseWords = reverseSentence(wordsList)
    reversedSentence = joinSentence(reverseWords)
    print('Reversed Sentence:',reversedSentence)

if __name__ == '__main__':
    main()