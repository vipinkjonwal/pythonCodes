list1 = [6,1,2,7,2,5,3,8,4]
list2 = [1,3,5,7,9,11]

def intersection(list1,list2,finalList=[]):
    lenList1 = len(list1)
    lenList2 = len(list2)

    index = 0
    for i in range(lenList1):
        for j in range(lenList2):
            if list1[i] == list2[j]:
                finalList.append(list1[i])

    return finalList

intersectionList = intersection(list1,list2)
print(intersectionList)


