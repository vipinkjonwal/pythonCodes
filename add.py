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
	print('Sum is ',mySum(number1,number2))

if __name__ == '__main__':
	main()

	