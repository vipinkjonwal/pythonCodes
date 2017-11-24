def computeSum(d,n):
    tempSum = 0
    for i in range(1,n+1):
        tempSum = tempSum + int(d*i)
    return tempSum


def main():
    d = str(input('Enter d: '))
    n = int(input('Enter n: '))
    finalSum = computeSum(d,n)
    print(finalSum)

if __name__ == '__main__':
    main()