def commonElements(list1,list2):
    set1 = set(list1)
    set2 = set(list2)

    commonElementsSet = set1 & set2

    return list(commonElementsSet)

lis1 = [1,2,3,4,5]
list2 = [3,4,5,6,7,8]
print(commonElements(lis1,list2))