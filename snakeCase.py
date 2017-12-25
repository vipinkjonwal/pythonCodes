def snakeCase(sentence):
    sentence = list(sentence)
    sentence[0] = sentence[0].lower()

    for i in range(len(sentence)):
        if sentence[i] == ' ':
            sentence[i] = '_'
        else:
            sentence[i] = sentence[i].lower()
    snakeCaseSentence = ''.join(sentence)
    return snakeCaseSentence

sentence = 'I love camelCases.'
print(snakeCase(sentence))


