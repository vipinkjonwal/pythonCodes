def partition(lst, start, end):
    '''
    Objective: To partition lists into two parts around pivot
    element
    Input Parameter: lst - list; start, end - numeric value
    Return Value: index - integer value (index of pivot element
                          in sorted list)
    '''
    pivotElement = lst[end]
    i = start-1
    for j in range(start, end):
        if lst[j]<= pivotElement:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[end] = lst[end], lst[i+1]
    return i+1

def quickSort(lst, start = 0, end = None):
    '''
    Objective: To sort the list lst in ascending order using quick
    sort
    Input Parameter: lst - list
    Return Value: sorted list
    '''
    if end == None: #Quick sort invoked for the first time
        end = len(lst) - 1
    if start<end:
        splitPoint = partition(lst, start, end)
        quickSort(lst, start, splitPoint-1)
        quickSort(lst, splitPoint+1, end)
    return lst

list = [3,7,1,13,9,2,6,4]
print(quickSort(list))