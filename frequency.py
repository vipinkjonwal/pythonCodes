def frequency(string):
    list1 = string.split(" ")
    newList = []

    for i in range(len(list1) - 1):
        sub = list1[i]
        if sub not in newList:
            newList.append(sub)
            if list1.count(sub) > 1:
                print(list1[i], ':', list1.count(sub))

string = """New to Python or wanna
 learn Python then you should read
 Python documentation or go to Internet."""
frequency(string)