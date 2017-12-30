def isPowerOfTwo(number):
    if number == 1:
        return True
    elif number % 2 != 0:
        return False
    else:
        return isPowerOfTwo(number//2)

print(isPowerOfTwo(14))
print(isPowerOfTwo(4096))