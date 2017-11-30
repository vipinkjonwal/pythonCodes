def palindrome(string,startIndex = 0):
    last = len(string) - 1

    if len(string) == 1 or len(string) == 0:
        return  True
    elif string[startIndex] == string[last]:
        startIndex += 1
        last -= 1
        return palindrome(string[startIndex:last+1])
    else:
        return False


choice = 'y'
while choice == 'y':
    string = str(input('Enter a string: '))
    boolValue = palindrome(string)

    if boolValue == True:
        print(string,'is a Palindrome.')
    else:
        print(string,'is NOT a Palindrome.')
    choice = input('Want to enter more (y/n): ')