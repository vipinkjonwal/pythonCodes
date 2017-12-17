def threeNumbers(number):
    numbers = []
    if number%3 == 0:
        numbers.extend([number/3 - 1,number/3,number/3 + 1])
        return numbers
    else:
        return -1

print(threeNumbers(12))
print(threeNumbers(11))
