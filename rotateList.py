def rotateList(givenList):
    temp = givenList[0]
    for i in range(len(givenList)-1):
        givenList[i] = givenList[i+1]
    givenList[len(givenList)-1] = temp
    return givenList

def listRotate(givenList):
    for i in range(len(givenList)-1):
        givenList[i],givenList[i+1] = givenList[i+1],givenList[i]
    return givenList

givenList = [1,2,3,4,5]
print(rotateList(givenList))

givenList = [1,2,3,4,5]
print(listRotate(givenList))
