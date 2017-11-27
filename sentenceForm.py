def sentence(subjectList,verbList,objectList):
    for i in range(len(subjectList)):
        for j in range(len(verbList)):
            for k in range(len(objectList)):
                print(subjectList[i],' ',verbList[j],' ',objectList[k],'.',sep="")


subjectList = ['I','You']
verbList = ['play','love']
objectList = ['Football','Programming']

sentence(subjectList,verbList,objectList)

'''
The function sentence takes three input lists of subject, verb and object.
It will print all possible statement of three words.
'''