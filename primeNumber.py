import math
import timeit
def isPrime(number):
    if number < 2:
        return False

    elif number % 2 == 0:
        return False

    elif number == 3:
        return True

    elif not((number + 1) % 6 == 0 or (number - 1) % 6 == 0):
        return False

    else:
        for i in range(5,int(math.sqrt(number)),2):
            if number % i == 0:
                return False
        return True

print(isPrime(3))

t = timeit.Timer(lambda: isPrime(7919))
print(t.timeit(number=100))