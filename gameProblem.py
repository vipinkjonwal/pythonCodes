def statusTop(givenList):
    finalList = []
    finalList.append(givenList[0])
    j = 0

    for i in range(1,len(givenList)):
        if givenList[i] < finalList[j]:
            finalList[j] = givenList[i]
            j += 1
        else:
            finalList.append(givenList[i])
        print(finalList)

    return finalList


givenList = [3,4,5,1,1,2]
print(statusTop(givenList))