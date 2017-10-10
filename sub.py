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

def mySub(number1,number2):
	'''
	Objective      : To compute the sum of given two numbers.
	Input Variabes :
	       number1 : integer - First number inputted by user.
	       number2 : integer - Second number inputted by user.

	Return Value   : Difference of given two numbers.
	'''
	#Approach      : Use of recursion and myIncrement function.
	if number2==0:
		return number1
	else:
		number1=pred.predecessor(number1)
		number1=mySub(number1,pred.predecessor(number2))
		return number1

def main():
	'''
	Objective      : To compute the difference of given two numbers.
	Input Variabes : None.
	Return Value   : None.
	'''
	#Approach      : Invoke mySum function.
	number1=int(input('Enter number1: '))
	assert number1>=0
	number2=int(input('Enter number2: '))
	assert number2>=0
	if number1>=number2:
		print('Difference is ',mySub(number1,number2))
	elif number2>number1:
		print('Difference is ',-1*mySub(number2,number1))	

if __name__ == '__main__':
	main()

	