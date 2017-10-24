def invertedTriangle(numberRows):
	'''
	Objective			: To print an inverted triangle.
	Input Parameters		:
			numberRows 	: integer-Number of rows inputted by user.
	Return value			: none
	'''
	#Approach			: Use of 'while' loop to print the triangle.
	
	numberSpaces=0									 
	numberStars=2*numberRows-1
	while numberStars>0:
		print(' '*numberSpaces,'*'*numberStars)
		numberStars-=2
		numberSpaces+=1			

def main():
	'''
	Objective			: To print an inverted triangle.
	Input Parameters		: none
	Return value			: none
	'''
	#Approach			: Invoke the function rightTriangle.

	numberRows=int(input('Enter the number of rows: '))
	invertedTriangle(numberRows)

if __name__ == '__main__':
	main()
