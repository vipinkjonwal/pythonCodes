import sys
def swap1(a,b):
    print('Method 1')
    print('Before Swapping : a : ',a,' & b : ',b)
    temp = a
    a= b
    b = temp
    print('After Swapping : a : ', a, ' & b : ', b)

def swap2(a, b):
    print('Method 2')
    print('Before Swapping : a : ', a, ' & b : ', b)
    a = a * b
    b = a / b
    a = a / b
    print('After Swapping : a : ', a, ' & b : ', b)

def swap3(a, b):
    print('Method 3')
    print('Before Swapping : a : ', a, ' & b : ', b)
    a = a + b
    b = a - b
    a = a - b
    print('After Swapping : a : ', a, ' & b : ', b)

def swap4(a, b):
    print('Method 4')
    print('Before Swapping : a : ', a, ' & b : ', b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print('After Swapping : a : ', a, ' & b : ', b)

print(sys.version)
swap1(1,2)
swap2(1,2)
swap3(1,2)
swap4(1,2)


