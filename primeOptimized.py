import math
import timeit
def primeNumber(number):
    #If number is less than or equal to 1, it's not Prime.
    if number <= 1:
        return False

    #2 is only Even Number which is Prime.
    elif number == 2:
        return True
    #Except 2, no even numbers are Prime. (Because, 2 will be a factor for sure.)
    elif number%2 == 0:
        return False

    else:
        for i in range(3,int(math.sqrt(number))):
            if number%i == 0:
                return False
        return True


t = timeit.Timer(lambda: primeNumber(7919))
print(t.timeit(number=100))