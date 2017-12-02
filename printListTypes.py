sampleList = [1,2,3,4,5,6,7,8]

#Using for loop to print the List.
for i in range(len(sampleList)):
    print(sampleList[i],sep=' ',end=' ')

#Using * to print the List.
print('\n')
print(*sampleList)

#Print the list by converting the list into string of integers.
print('\n')
print(str(sampleList)[1:-1])

#Print the list by converting the list into string using map.
print('\n')
print(' '.join(map(str,sampleList)))