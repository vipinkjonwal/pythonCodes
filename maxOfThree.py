import timeit

def maxTwo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def maxThree(num1,num2,num3):
    return maxTwo(maxTwo(num1,num2),num3)

def maximumThree(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


t1 = timeit.Timer(lambda: maxThree(22,13,11))
print('Method 1:',t1.timeit())

t2 = timeit.Timer(lambda: maximumThree(22,13,11))
print('Method 2:',t2.timeit())


