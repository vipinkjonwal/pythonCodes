def initializeMatrix():
    row,column = 3,3
    matrix = [[0 for x in range(row)] for y in range(column)]
    return matrix

def populateMatrix(dummyMatrix):
    dummyMatrix[0][0] = int(input('0,0th Intensity: '))
    dummyMatrix[0][1] = int(input('0,1th Intensity: '))
    dummyMatrix[0][2] = int(input('0,2th Intensity: '))
    dummyMatrix[1][0] = int(input('1,0th Intensity: '))
    dummyMatrix[1][1] = int(input('1,1th Intensity: '))
    dummyMatrix[1][2] = int(input('1,2th Intensity: '))
    dummyMatrix[2][0] = int(input('2,0th Intensity: '))
    dummyMatrix[2][1] = int(input('2,1th Intensity: '))
    dummyMatrix[2][2] = int(input('2,2th Intensity: '))
    return dummyMatrix

def binaryMatrix(intensityMatrix):
    row, column = 3, 3
    binaryValueMatrix = [[0 for x in range(row)] for y in range(column)]

    for i in range(3):
        for j in range(3):
            if (intensityMatrix[i][j] < intensityMatrix[1][1]):
                binaryValueMatrix[i][j] = 0
            elif (intensityMatrix[i][j] >= intensityMatrix[1][1]):
                binaryValueMatrix[i][j] = 1
    return binaryValueMatrix

def calculateDecimalEquivalent(binaryValueMatrix):
    decimalEquivalent = binaryValueMatrix[0][0]*(2**7) +\
                        binaryValueMatrix[0][1]*(2**6) +\
                        binaryValueMatrix[0][2]*(2**5) +\
                        binaryValueMatrix[1][2]*(2**4) +\
                        binaryValueMatrix[2][2]*(2**3) +\
                        binaryValueMatrix[2][1]*(2**2) +\
                        binaryValueMatrix[2][0]*(2**1) +\
                        binaryValueMatrix[1][0]*(2**0)
    return decimalEquivalent

initialMatrix = initializeMatrix()
intensityMatrix = populateMatrix(initialMatrix)
binaryValueMatrix = binaryMatrix(intensityMatrix)
decimalEquivalent = calculateDecimalEquivalent(binaryValueMatrix)
print(decimalEquivalent)