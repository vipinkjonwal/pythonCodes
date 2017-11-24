def convert(string):
    length = len(string)
    if length < 3:
        return string

    tempTestString = string[length-3:length]

    if tempTestString == 'ing':
        return string+'ly'
    else:
        return string+'ing'

def main():
    string = input('Enter a string: ')
    convertedString = convert(string)
    print('Converted string is',convertedString)

if __name__ == '__main__':
    main()