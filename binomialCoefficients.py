import math

def combination(n,r):
    return int((math.factorial(n))/(math.factorial(r)*math.factorial(n-r)))

def binomialCoefficients(n):
    for i in range(n+1):
        print(combination(n,i),' ',end='')

binomialCoefficients(10)