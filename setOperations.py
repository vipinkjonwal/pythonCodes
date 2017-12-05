def unionOperation(list1,list2):
    index1 = 0
    index2 = 0
    index = 0
    unionList = []
    while (index1 < len(list1)) and (index2 < len(list2)):
        if list1[index1] < list2[index2]:
            print(list1[index1])
            index1 += 1
            index += 1
        elif list1[index1] > list2[index2]:
            print(list2[index2])
            index2 += 1
            index += 1
        else:
            print(list1[index1])
            index1 += 1
            index2 += 1

    return unionList
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7,8]
finalList = unionOperation(list1,list2)
print(finalList)