y = [245,312,279,308,199,219,405,324,319,255]
x = [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]

def mean(x):
    return sum(x)/float(len(x))

def variance(x):
    var = sum([(i - mean(x))**2 for i in x])
    return var/float(len(x)-1)

def covariance(x,y):
    meanX = mean(x)
    meanY = mean(y)
    cov = 0
    for i in range(len(x)):
        cov += (x[i] - meanX) * (y[i] - meanY)
    return cov/float(len(x)-1)

def calculateCoefficients(x,y):
    b1 = covariance(x,y)/variance(x)
    b0 = mean(y) - (b1*mean(x))
    return [b0,b1]

def testNewData(dataPoint):
    global x
    global y
    coefficients = calculateCoefficients(x,y)
    b1 = coefficients[1]
    b0 = coefficients[0]
    yCalc = b0 + (b1*dataPoint)
    yCalc= round(yCalc,6)
    return yCalc

print(testNewData(2000))


