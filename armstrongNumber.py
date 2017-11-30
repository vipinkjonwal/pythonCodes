def armstrongNumber(number):
    power = len(str(number))
    totalSum = 0

    tempNum = number
    while tempNum > 0:
        digit = tempNum%10
        totalSum += digit**power
        tempNum //= 10

    if totalSum == number:
        return True
    else:
        return False

number = int(input('Enter a number: '))
boolValue = armstrongNumber(number)

if boolValue == True:
    print(number,'is an Armstrong Number.')
else:
    print(number,'is NOT an Armstrong Number.')