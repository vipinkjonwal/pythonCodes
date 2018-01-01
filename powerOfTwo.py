import timeit
def isPowerOfTwo(number):
    if number == 1:
        return True
    elif number % 2 != 0:
        return False
    else:
        return isPowerOfTwo(number//2)

t = timeit.Timer(lambda:isPowerOfTwo(8192))
print(t.timeit(number=1000))