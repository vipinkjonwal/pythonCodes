import turtle

def fibonacci(position):
        
    '''
    Objective			: To calculate fibonacci number at position 'position'
    Input Variables		:
                      position  : Given position, the position at which fibonacci to be calculated.
    Return Value		: Corresponding fibonacci number at position 'position'
    '''
    # Approach			: Recursion is used to find fibonacci number at position'position'.
	
    if position == 0 or position == 1:
        return 1
    else:
        return fibonacci(position-1) + fibonacci(position-2)
    
def drawCircle(number):
    '''
    Objective			: To draw the golden ratio circle 'number' times.
    Input Variables		:
		      position  : Given number, number of level it draws the circle.
    Return Value		: None.
    '''
    # Approach			: Turtle package is used to draw circle, method used 'turtle.circle(...)'.
    

    fibonacciList = []
    for i in range(number):
        fibonacciList.append(fibonacci(i))

    for i in fibonacciList:
        turtle.circle(i,90)

if __name__ == '__main__':
    number = int(input("Enter the number: "))
    drawCircle(number)
