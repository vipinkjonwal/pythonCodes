def flatterList(givenList,totalSum=0,index=0):

    if len(givenList) == index:
        return totalSum
    elif type(givenList[index]) == int:
        totalSum += givenList[index]
        index=index+1
        return flatterList(givenList,totalSum,index)
    elif type(givenList[index]) == list:
        return flatterList(givenList[index],totalSum)

def main():
    givenList=[1,2,[3,4,7,10,13],13]
    print(flatterList(givenList))

if __name__ == '__main__':
    main()
