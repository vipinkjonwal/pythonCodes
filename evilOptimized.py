def checkEvil(number):
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
