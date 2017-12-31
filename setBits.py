def setBits(number,count = 0):
    if number == 0:
        return count
    else:
        if number % 2 == 1:
            count += 1
        number = number // 2
        return setBits(number,count)

def powerOfTwo(number):
    if setBits(number) == 1:
        return True
    else:
        return False

