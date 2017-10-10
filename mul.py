import sys
import pred

def myIncrement(number):
	'''
	Objective      : To compute the increment of given number.
	Input Variabes :
	        number : Number of which increment is to be computed.
	Return Value   : Incremented value of given number.
	'''
	#Approach      : Add 1 to given number.
	return number+1

def mySum(number1,number2):
	'''
	Objective      : To compute the sum of given two numbers.
	Input Variabes :
	       number1 : integer - First number inputted by user.
	       number2 : integer - Second number inputted by user.

	Return Value   : Sum of given two numbers.
	'''
	#Approach      : Use of recursion and myIncrement function.
	if number2==0:
		return number1
	else:
		return mySum(myIncrement(number1),pred.predecessor(number2))

def myMul(number1,number2):
	'''
	Objective		: To multiply two given numbers.
	Input Variabes :
	       number1 : integer - First number inputted by user.
	       number2 : integer - Second number inputted by user.

	Return Value   : Product of given two numbers.
	'''
	#Approach      : Use of recursion, myIncrement and mySum function.
	
	if number1 == 0 or number2 ==0:
		return 0
	elif number2==1:
		return number1
	else:
		return mySum(number1,myMul(number1,pred.predecessor(number2)))

def main():
	'''
	Objective      : To compute the sum of given two numbers.
	Input Variabes : None.
	Return Value   : None.
	'''
	#Approach      : Invoke mySum function.
	number1=int(input('Enter number1: '))
	assert number1>=0
	number2=int(input('Enter number2: '))
	assert number2>=0
	
	if number2>number1:
		tempNum=number1
		number1=number2
		number2=tempNum

	print('Product is ',myMul(number1,number2))

if __name__ == '__main__':
	main()

	