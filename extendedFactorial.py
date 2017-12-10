import scipy.integrate as integrate
import numpy as np

def gammaFunction(alpha):
    def function(x):
        return (x**(alpha-1))*(np.exp(-x))
    result = integrate.quad(function, 0, np.inf)
    return result[0]

alpha = float(input('Enter a positive real number: '))
while alpha < 0:
    print('ERROR: You have inputted negative number. Try again.')
    alpha = float(input('Enter a positive real number: '))
ans = round(gammaFunction(alpha+1),8)
print('Factorial of',alpha,'is',ans)
