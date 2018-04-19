from tkinter import *
from random import *
import time
import pandas as pd

def sender_network():
    data = pd.read_csv('dataToBeSend.csv')
    frameData = data.iloc[:,:].values
    return frameData

def sender_physical(frame):
    random = randint(1 ,4)
    if(random == 3):
        time.sleep(3)
        frame_lost()
        print('Sending same again...')
        sender_physical(frame)
    else:
        receiver()
        return

def receiver():
    print('Data received at physical layer of receiver...')
    return

def acknowledgement_lost():
    print('Acknowledgement lost...')
    return

def acknowledgement_received():
    print('Acknowledgement sent.')
    return
def frame_lost():
    print('Frame lost...')

def wait_for_event():
    frame = sender_network()
    numFrames = int(input('How many frames you want to send: '))
    for i in range(0,numFrames):
        print('Sending',i+1,'th frame...')
        sender_physical(frame[i])
        random = randint(1 ,4)
        if(random == 3):
            time.sleep(3)
            acknowledgement_lost()
            print('Sending same frame again...')
            sender_physical(frame[i])
        else:
            acknowledgement_received()
        print(i+1,'th frame sent successfully.\n')
wait_for_event()

