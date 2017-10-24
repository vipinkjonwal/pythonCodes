def shiftHeaviest(givenList,index,tempIndex=0):
	'''
	Objective		: To shift the heaviest element from index 0 to index 'index-1' at the index 'index'.
	Input Parameters	: 
		givenList	: List entered by the user.
		    index       : Index to which heaviest element is to be shifted.
		tempIndex	: DEFAULT - 0 ; For iterations.
	Return Value		: None.
	'''
	#Approach		: To swap the number to right if it is larger than the other number 
	#					  and recursively doing till it reaches to desired index. 

	if tempIndex!=index:
		if givenList[tempIndex]>givenList[tempIndex+1]:
			tempNumber=givenList[tempIndex]
			givenList[tempIndex]=givenList[tempIndex+1]
			givenList[tempIndex+1]=tempNumber
			tempIndex=tempIndex+1
			shiftHeaviest(givenList,index,tempIndex)
		else:
			tempIndex=tempIndex+1
			shiftHeaviest(givenList,index,tempIndex)
	else:
		return

def main():
	'''
	Objective		: To shift the heaviest element from index 0 to index 'index-1' at the index 'index'.
	Input Parameters	: None.
	Return Value		: None.
	'''
	#Approach		: Invoke the shiftHeaviest function.

	givenList=[int(x) for x in input('Enter the elements of the list: ').split()]
	print('You have entered: ',givenList,sep="")
	index=int(input('Enter the index to which heaviest element is to be shifted: '))
	assert index<=len(givenList)-1,'Index must be less than length of given list.'
	shiftHeaviest(givenList,index)
	print('List becomes ',givenList,sep="")

if __name__ == '__main__':
	main()
