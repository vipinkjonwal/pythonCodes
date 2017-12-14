def computeSum(d,n,sum=0):
    if n == 1:
        return sum + d
    else:
        return int(str(d)*n) + computeSum(d,n-1,sum)

print(computeSum(9,3))