def divideByZeroCatch():
    numerator = int(input('Enter the numerator: '))
    denominator = int(input('Enter the denominator: '))
    fraction = 0
    try:
        fraction = numerator/denominator
    except ZeroDivisionError:
        print('Divide by Zero not allowed.')
    return fraction

answer = divideByZeroCatch()
print(answer)
