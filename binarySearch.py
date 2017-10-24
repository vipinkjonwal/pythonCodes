def findIndex(givenList,lower,upper,element):
	'''
	Objective			: To find the index of an element from a list using binary search algorithm.
	Input Parameters		:
			givenList	: User entered list in sorted order.
			lower		: Lower index of list under consideration.
			upper		: Upper index of list under consideration.
			element     	: Element to be searched.
	Return Value			: Index of element to be found or -1 if element not found.
	'''
	#Approach			: Recursion on findIndex function.

	middle=(lower+upper)//2
	if lower<=upper:
		if givenList[middle]==element:
			return middle
		elif givenList[middle]<element:
			return findIndex(givenList,middle+1,upper,element)
		elif givenList[middle]>element:
			return findIndex(givenList,lower,middle-1,element)
	else:
		return -1

def binarySearch(givenList,element):
	'''
	Objective			: To search an element from a list using binary search algorithm.
	Input Parameters		:
			givenList	: User entered list in sorted order.
			element     	: Element to be searched.
	Return Value			: Index of element to be found or -1 if element not found.
	'''
	#Approach			: Invoke findIndex function to find the index of given element to be search.

	lower=-1
	upper=len(givenList)-1
	return findIndex(givenList,lower,upper,element)

def main():
	'''
	Objective			: To search an element from a list using binary search algorithm.
	Input Parameters		: None.
	Return Value			: None.
	'''
	#Approach			: Invoke binarySearch function.

	givenList=[int(x) for x in input('Enter the elements of the list (In sorted order): ').split()]
	print('You have entered: ',givenList,sep="")
	element=int(input('Enter the element to be search: '))
	returnIndex=binarySearch(givenList,element)		
	if returnIndex==-1:
		print('Element ',element,' not found in given list.',sep="")
	else:
		print('Element ',element,' found at index ',returnIndex,sep="")

if __name__ == '__main__':
	main()
