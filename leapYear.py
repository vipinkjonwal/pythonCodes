def checkLeap(year):
	leap = False
	if ((year%4)==0 and (year%100!=0)):
		leap = True
	elif ((year%100)==0 and (year%400==0)):
		leap = True
	else:
		leap = False
	return leap

def main():
	year = int(input('Enter an year : '))
	leapYear = checkLeap(year)

	if leapYear==True:
		print(year,' is a leap year.')
	else:
		print(year,' is not a leap year.')

if __name__ == '__main__':
	main()