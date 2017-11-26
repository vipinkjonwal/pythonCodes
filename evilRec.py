def evilNumber(number,count = 0):
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

print(evilNumber(12))
print(evilNumber(11))
print(evilNumber(1))
print(evilNumber(25))
