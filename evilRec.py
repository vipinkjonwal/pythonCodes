def evilNumber(number,count = 0):
    '''
    Objective           : To check whether the number is Evil Number or not.
    Input Variables     :
           :param number: Given number to check if evil or not.
            :param count: Default - 0 | To maintain count of number of 1's.
    Return Value        : Bool Value, whether number if Evil or Not
    '''
    if number == 0:
        if count%2 == 0:
            return True
        else:
            return  False
    else:
        if number%2 == 1:
            count += 1
        number = number//2
        return(evilNumber(number,count))

# Test Cases
print(evilNumber(12))
print(evilNumber(11))
print(evilNumber(1))
print(evilNumber(25))

'''
Problem : To find whether a given number is Evil Number or Not.
A number is called Evil Number if it contains even number of 1's
in its Binary Equivalent.
For example : 12, in binary is 1100, contains 2 1's, hence Evil.
              11, in binary is 1011, contains 3 1's, hence NOT Evil.  
'''