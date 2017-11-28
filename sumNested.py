def sumList(givenList,totalSum = 0,i = 0):
    if len(givenList) == i:
        return totalSum
    else:
        totalSum += givenList[i]
        i += 1
        return sumList(givenList,totalSum,i)

def sumNested(givenList, totalSum = 0,i = 0):
    if len(givenList) == i:
        return totalSum
    elif type(givenList[i]) == int:
        totalSum += givenList[i]
        i += 1
        return sumNested(givenList,totalSum,i)
    elif type(givenList[i]) == list:
        tempSum = sumList(givenList[i])
        totalSum += tempSum
        return sumNested(givenList,totalSum,i+1)


givenList = [1,[5],6,[1,2,4],5]
totalSum = sumNested(givenList)
print('Given List',givenList)
print('Sum of Elements of Nested List is',totalSum)