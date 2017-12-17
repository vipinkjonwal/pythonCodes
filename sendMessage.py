import fbchat
from getpass import getpass
username = str(input("Enter Username: "))
client = fbchat.Client(username,getpass())
numFriends = int(input("Number of friends: "))
for i in range(numFriends):
    name = str(input("Name: "))
    friends = client.getUsers(name)
    friend = friends[0]
    msg = str(input("Enter message: "))
    sent = client.send(friend.uid,msg)
    if sent:
        print("Message Sent!")
