def shiftZero(givenList):
    nonZeroCount = 0
    finalList = []
    for i in range(len(givenList)):
        if givenList[i] != 0:
            finalList.append(givenList[i])
            nonZeroCount += 1

    for i in range(nonZeroCount,len(givenList)):
        finalList.append(0)
        
    return finalList


givenList = [1,2,0,4,3,0,5,0]
finalList = shiftZero(givenList)
print(finalList)