def splitEvenOdd(givenList):
    oddList = []
    evenList = []

    for i in givenList:
        if i%2 != 0:
            oddList.append(i)
        else:
            evenList.append(i)

    return [oddList,evenList]

givenList = [8,12,15,9,3,11,26,23]
oddList = splitEvenOdd(givenList)[0]
evenList = splitEvenOdd(givenList)[1]

print('Given List:',givenList)
print('Odd List:',oddList)
print('Even List:',evenList)
