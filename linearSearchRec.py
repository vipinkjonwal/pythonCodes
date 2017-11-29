def linearSearch(givenList,element):
    if len(givenList) == 0:
        return False
    else:
        if givenList[0] == element:
            return True
        else:
            return linearSearch(givenList[1:],element)

givenList = [11,27,7,12,4,19,10,34]
element = int(input('Enter the element: '))
boolValue = linearSearch(givenList,element)

if boolValue == True:
    print(element,'is present in the list.')
else:
    print(element, 'is NOT present in the list.')