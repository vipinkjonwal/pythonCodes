def unionOperation(list1,list2):
    index1 = 0
    index2 = 0
    unionList = []
    unionList.extend(list1)

    for i in range(len(list2)):
        if list2[i] not in unionList:
            unionList.append(list2[i])
    return unionList


list1 = [1,2,3,4,5]
list2 = [6,7,8,4,5,3,2,1,3,9]
finalList = unionOperation(list1,list2)
print(finalList)