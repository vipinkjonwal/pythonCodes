def fibonacci(number):
    '''
    Objective                : Computes the Fibonacci Number at position 'number'
    Input Variables          :
                :param number: Given number at which position Fibonacci Number is expected.
    Return Value             : Fibonacci Number at position 'number'
    '''
    if number == 0 or number == 1:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)

number = int(input('How many Fibonacci Numbers you want: '))
for i in range(number):
    print(fibonacci(i),end=" ")