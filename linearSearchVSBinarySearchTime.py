import timeit

def linearSearch(givenList,element):
    for i in range(len(givenList)):
        if givenList[i] == element:
            return i
    return -1

def forLoop():
    for i in range(100000):
        i += 1

def whileLoop():
    i = 0
    while i < 100000:
        i += 1

t1 = timeit.Timer(lambda: linearSearch([2,1,3,7,5,4,6],2))
print(t1.timeit(10000))

t2 = timeit.Timer(lambda: forLoop())
print('For Loop (3.6.3) : ',t2.timeit(100))

t3 = timeit.Timer(lambda: whileLoop())
print('While Loop (3.6.3) : ',t3.timeit(100))

