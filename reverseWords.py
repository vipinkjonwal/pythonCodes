def reverseWords(givenString):
    givenStringList = givenString.split(' ')
    reversedString = ''
    for i in givenStringList:
        temp = list(i)
        temp.reverse()
        revWord = ''.join(temp)
        reversedString += revWord
        reversedString += ' '

    return reversedString

givenString = 'Learning Python is nice practice'
print('Given String: ',givenString)
print('Output: ',reverseWords(givenString))