import matplotlib.pyplot as plt
def square(x, y):
	'''
	Objective: To plot a square
	Input Parameters: x, y - lists of x coordinates and y
	coordinates respectively
	Return Value: None
	'''
	plt.plot(x, y, 'bo--')

def main():
	'''
	Objective: To plot a square based on user input
	Input Parameter: None
	Return Value: None
	'''
	size = int(input('Enter size of the square: '))

	for i in range(1,size+1):
	    x = [i, size-i, size-i, i, i]
	    y = [i, i, size-i, size-i, i]
	    square(x, y)
	
	plt.title('Square')
	plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
	plt.grid()
	plt.show()

if __name__ == '__main__':
	main()
