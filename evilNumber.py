def evilNumber(number):
	count = 0
	binNumber  = bin(number)
	length = len(binNumber)

	for i in range(2,length):
		if binNumber[i] == '1':
			count += 1

	if count % 2 == 0:
		return True
	else:
		return False	

def main():
	number = int(input("Enter a number: "))
	boolAnswer = evilNumber(number)
	
	if boolAnswer == True:
		print(number, 'is an Evil Number.')
	else:
		print(number, 'is not an Evil Number.')

if __name__ == '__main__':
	main()
