def myIncrement(number):
	'''
	Objective		: To compute the increment of given number.
	Input Variables	:
			number  : integer - number of which increment is to be computed.
	Return value    : Increment value of given number, by 1
	'''
	#Approach		: Add 1 to the given number and return it.
	return number+1

def predecessor(number,tempNumber=0):
	'''
	Objective		: To find the predecessor of given number.
	Input Variables	:
			number  : integer - number of which predecessor is to be computed.
		tempNumber  : integer - a temporary number used for purpose of recursion.
	Return value    : Predecessor of given number.
	'''
	'''
	Approach		: Recursion and use of myIncrement function. 
					  Concept being if y is successor of x then predecessor of y is x.
	'''
	if number==0 or number==1:
		return 0
	else:
		if myIncrement(tempNumber)==number:
			return tempNumber
		else:
			tempNumber=tempNumber+1
			return predecessor(number,tempNumber)

def main():
	'''
	Objective		: To find the predecessor of given number inputted by user.
	Input Variables : None.
	Return value    : None. 
	'''
	#Approach       : Invoke predecessor function.
	number=int(input('Enter the number: '))
	predValue=predecessor(number)
	print('Predecessor of',number,'is',predValue)

if __name__ == '__main__':
	main()
