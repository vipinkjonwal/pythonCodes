def rotateList(givenList):
    temp = givenList[0]
    for i in range(len(givenList) - 1):
        givenList[i] = givenList[i + 1]
    givenList[len(givenList) - 1] = temp
    return givenList

def rotateKFolds(givenList,k):
    for i in range(k):
        rotateList(givenList)

    return givenList

givenList = [1,2,3,4,5]
print(rotateKFolds(givenList,3))