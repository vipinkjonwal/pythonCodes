def merge(list1, list2):
    sortedList = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            sortedList.append(list1[0])
            list1.remove(list1[0])
        else:
            sortedList.append(list2[0])
            list2.remove(list2[0])
    if len(list1) == 0:
        sortedList += list2
    else:
        sortedList += list1
    return sortedList

def mergeSort(list):
    if len(list) == 0 or len(list) == 1:
        return list
    else:
        mid = len(list)//2
        list1 = mergeSort(list[:mid])
        list2 = mergeSort(list[mid:])
        return merge(list1,list2)

print(mergeSort([2,4,1,6,3,5]))