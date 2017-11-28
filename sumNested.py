def sumNested(givenList, totalSum = 0,i = 0):
    if len(givenList) == i:
        return totalSum
    elif type(givenList[i]) == int:
        totalSum += givenList[i]
        i += 1
    elif type(givenList[i]) == list:
       return sumNested(givenList[i],totalSum,i)


givenList = [1,2,3,[4,5],6,7,8,9,10]
totalSum = sumNested(givenList)
print(totalSum)