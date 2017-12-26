def roundToTen(number):
    tempNumber = (number // 10) * 10
    newTemp = tempNumber + 10
    if newTemp - number < number - tempNumber:
        return newTemp
    else:
        return tempNumber

