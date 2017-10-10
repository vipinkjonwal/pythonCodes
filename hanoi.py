def towerOfHanoi(numDisks, source, spare, destination):
	'''
	Objective		: To solve the problem of tower of hanoi.
	Input Variable	:
		numDisks	: integer - Number of disks.
		source		: source tower.
		spare		: spare tower.
		destination	: destination tower.
	Return value	: None.
	'''
	#Approach		: Using recursion.

	assert numDisks>0
	if numDisks==1:
		print('Move a disk from',source,'to',destination)
	else:
		towerOfHanoi(numDisks-1,source,destination,spare)
		print('Move a disk from',source,'to',destination)
		towerOfHanoi(numDisks-1,spare,source,destination)

def main():
	'''
	Objective		: To solve the problem of tower of hanoi.
	Input Variable	: None.
	Return value	: None.
	'''
	#Approach		: Invoke towerHanoiFunction.

	source='A'
	spare='B'
	destination='C'
	print('\n\t\t***** TOWERS OF HANOI *****\n')
	numDisks=int(input('Enter the number of disks: '))
	towerOfHanoi(numDisks,source,spare,destination)
	
if __name__ == '__main__':
		main()	