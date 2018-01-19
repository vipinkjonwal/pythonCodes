def removeDuplicate(givenList):
    '''
    Objective               : To remove duplicates from the list.
    Input Parameters
                   givenList: Given list with duplicate values.
    Return Value            : Given list with duplicates removed.
    '''
    # Approach              : Set properties is used to remove duplicates.

    return list(set(givenList))

# Test Case
givenList = [1,2,3,4,5,4,3,2,3,4,5,6]
print(removeDuplicate(givenList))
