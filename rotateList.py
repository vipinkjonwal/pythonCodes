import timeit
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
t1 = timeit.Timer(lambda: rotateList(givenList))
print('Method 1:',t1.timeit())

givenList = [1,2,3,4,5]
print(listRotate(givenList))
t2 = timeit.Timer(lambda: listRotate(givenList))
print('Method 2:',t2.timeit())
