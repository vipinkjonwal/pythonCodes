import timeit
def isPowerOfTwo(number):
    if ((number&(~(number-1))) == number):
        return True
    else:
        return False

t = timeit.Timer(lambda: isPowerOfTwo(8192) )
print(t.timeit(number=1000))