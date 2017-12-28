import timeit

def swap1(a,b):
    temp = a
    a= b
    b = temp

def swap2(a, b):
    a = a * b
    b = a / b
    a = a / b

def swap3(a, b):
    a = a + b
    b = a - b
    a = a - b

def swap4(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

def swap5(a,b):
    return b,a

t1 = timeit.Timer(lambda: swap1(1,2))
print('Method 1 (Using Temp):',t1.timeit())

t2 = timeit.Timer(lambda: swap2(1,2))
print('Method 2 (Using * and /):',t2.timeit())

t3 = timeit.Timer(lambda: swap3(1,2))
print('Method 3 (Using + and -):',t3.timeit())

t4 = timeit.Timer(lambda: swap4(1,2))
print('Method 4 (Using XOR):',t4.timeit())

t5 = timeit.Timer(lambda: swap5(1,2))
print('Method 5 (Using Python Methods):',t5.timeit())



'''
swap1(1,2)
swap2(1,2)
swap3(1,2)
swap4(1,2)
'''

