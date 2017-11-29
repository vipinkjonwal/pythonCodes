def linearSearch(givenList,element,position=0):
    if len(givenList) == 0:
        return -1
    else:
        if givenList[0] == element:
            return position
        else:
            position += 1
            return linearSearch(givenList[1:],element,position)

givenList = [11,27,7,12,4,19,10,34]
element = int(input('Enter the element: '))
positionElement = linearSearch(givenList,element)

print('Given List: ',givenList)
if positionElement == -1:
    print(element,'is NOT present in the list.')
else:
    print(element,'is present in the list at location',positionElement+1)