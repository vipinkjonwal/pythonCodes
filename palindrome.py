def palindrome(string):
    i = 0
    j = len(string)-1

    while(i < j):
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

choice = 'y'
while choice == 'y':
    string = str(input('Enter a string: '))
    boolValue = palindrome(string)

    if boolValue == True:
        print(string,'is a Palindrome.')
    else:
        print(string,'is NOT a Palindrome.')
    choice = input('Want to enter more (y/n): ')