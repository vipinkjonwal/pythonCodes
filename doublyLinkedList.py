from os import listdir
from os.path import isfile,join

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None

    def insert(self,newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            newNode.prev = self.head
            return

        temp = self.head

        while(temp.next is not self.head):
            temp = temp.next

        newNode.prev = temp
        temp.next = newNode
        self.head.prev = newNode
        newNode.next = self.head


    def display(self):
        temp = self.head
        while(temp is not self.head.prev):
            print(temp.data," ")
            temp = temp.next
        print(self.head.prev.data)


    def getNext(self):
        return self.head.next.data


    def getPrev(self):
        return self.head.prev.data


    def getFileName(self,path):
        files = [f for f in listdir(path) if isfile(join(path,f))]
        mp3Files = []
        for i in files:
            if '.mp3' in i:
                mp3Files.append(i)
        return mp3Files


dlist = Doublylinkedlist()
listFiles = dlist.getFileName("C:\\Users\\vkjof\Desktop\\Networks Final")
for i in listFiles:
    dlist.insert(i)
dlist.display()

d1 = dlist.getNext()
d2= dlist.getPrev()
print("present",dlist.head.data)
print("next",d1)
print("prev",d2)
