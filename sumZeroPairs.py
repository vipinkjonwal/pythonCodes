import timeit
def findPair(givenList):
    pairList = []
    for i in givenList:
        if -i in givenList:
            pairList.append((i,-i))
            givenList.remove(i)
    return pairList

givenList = [-3,1,4,6,-2,3,2,-1,7,-4]
pairsList = findPair(givenList)
print(pairsList)

t = timeit.Timer(lambda: findPair(givenList))
print(t.timeit(number=10000))