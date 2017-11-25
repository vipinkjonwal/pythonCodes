def checkEvil(number):
    '''
    Objective            : To check whether given number is evil or not.
    Input Variables      :
            :param number: Given number to check if evil or not.
    Return Value         : Bool Value - True or False, if Evil the True else False
    '''
    #Approach            : Count the number of 1's in it's binary form using traditional
    #                      method of finding binary equivalent.

    count = 0
    while (number != 0):
        if number % 2 == 1:
            count += 1
        number = number // 2

    if count % 2 == 0:
        return True
    else:
        return False


def main():
    number = int(input('Enter a number: '))
    isEvil = checkEvil(number)
    print(number, 'in Binary is', bin(number))
    if isEvil == True:
        print(number, 'is Evil Number.')
    else:
        print(number, 'is not Evil Number.')


if __name__ == '__main__':
    main()
