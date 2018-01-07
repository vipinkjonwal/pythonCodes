def segregate(givenList):
    zeroLen = 0
    segregateList = []
    for i in givenList:
        if i == 0:
            segregateList.append(i)
            zeroLen += 1

    for i in range(len(givenList)-zeroLen):
        segregateList.append(1)

    return segregateList


givenList = [0,1,1,0,0,1,0,0,1,1,0]
print(segregate(givenList))