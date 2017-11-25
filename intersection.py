list1 = [6,1,2,7,2,5,3,8,4]
list2 = [1,3,5,7,9,11]

def intersection(list1,list2,finalList=[]):
    '''
    Objective           : To find the intersection of two lists.
    Input Parameters    :
            :param list1: Given List 1
            :param list2: Given List 2
        :param finalList: Default - Null List, will contain intersection of given lists
    Return Value        : finalList, the intersection of two lists.
    '''
    #Approach           : Iterative approach is used.

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


