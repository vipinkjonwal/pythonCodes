import timeit
def findPairs(givenList):
    pairsList = []

    for i in givenList:
        for j in givenList:
            if i+j == 0:
                pairsList.append((i,j))
                givenList.remove(j)

    return pairsList

givenList = [-3,1,4,6,-2,3,2,-1,7,-4]
pairsList = findPairs(givenList)
print(pairsList)

t = timeit.Timer(lambda: findPairs(givenList))
print(t.timeit(number=10000))