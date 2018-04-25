"""
Program         : Media Player Stimulation
Author(s)       : 1. Smrity Chaudhary
                  2. Vipin Kumar
"""

# Import necessary libraries.
from tkinter import *
import pygame

# Import doublyLinkedList file.
from doublyLinkedList import *

# Creating an object of DoublyLinkedList Class.
dlist = Doublylinkedlist()

# Creating object of Tk class.
root = Tk()
pygame.mixer.init()


# -----------------------------------------------------------------------------
# Global Variables for images
backgroundImage = PhotoImage(file="Images/background.png")
stopPhoto = PhotoImage(file="Images/stop.png")
playPhoto = PhotoImage(file="Images/play.png")
pausePhoto = PhotoImage(file="Images/pause.png")
playAgainPhoto = PhotoImage(file="Images/playagain.png")
nextPhoto = PhotoImage(file="Images/next.png")
prevPhoto = PhotoImage(file="Images/prev.png")
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Member Functions

def playMusic():
    '''
    Objective           : Play the music specified by head of dlist.
    Input Variables     : None
    Return Value        : None
    Approach            : Use pygame.mixer.music to load and play the
                          song.
    '''
    pygame.mixer.music.load(dlist.head.data)
    pygame.mixer.music.play()


def stopMusic():
    '''
    Objective           : Stop the playing music.
    Input Variables     : None
    Return Value        : None
    Approach            : Use pygame.mixer.music to stop the song.
    '''
    pygame.mixer.music.stop()


def pauseMusic():
    '''
    Objective           : Pause the currently playing song.
    Input Variables     : None
    Return Value        : None
    Approach            : Use pygame.mixer.music to pause the song.
    '''
    pygame.mixer.music.pause()


def unpauseMusic():
    '''
    Objective           : Unpause the music which is last paused.
    Input Variables     : None
    Return Value        : None
    Approach            : Use pygame.mixer.music to unpause the song.
    '''
    pygame.mixer.music.unpause()


def prevMusic():
    '''
    Objective           : Play the previous song from the dlist.
    Input Variables     : None
    Return Value        : None
    Approach            : Use pygame.mixer.music to load and play the
                          song.
    '''
    pygame.mixer.music.load(dlist.getPrev())
    pygame.mixer.music.play()


def nextMusic():
    '''
    Objective           : Play the next song from the dlist.
    Input Variables     : None
    Return Value        : None
    Approach            : Use pygame.mixer.music to load and play the
                          song.
    '''
    pygame.mixer.music.load(dlist.getNext())
    pygame.mixer.music.play()


def loadMediaPlayer(dirPath):
    '''
    Objective           : Load the name of mp3 file from specified path to dlist.
    Input Variables     : None
    Return Value        : None
    Approach            : Use GetFileName(...) to load mp3 files from specified path.
    '''
    listFiles = dlist.getFileName(dirPath)
    for i in listFiles:
        dlist.insert(i)


def mediaPlayerCanvas():
    '''
    Objective           : Draw the media player canvas.
    Input Variables     : None
    Return Value        : None
    Approach            : To draw the canvas, we have used canvas object and
                          Tkinter objects. Buttons are created using Button(...)
                          method.
    '''
    root.title("SV Music")
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='Images/mediaPlayer.png'))
    canvas = Canvas(root,width = 300,height = 300)
    canvas.pack()
    canvas.configure(background='black')

    canvas.create_image(0,0,image = backgroundImage)

    root.configure(background='black')


    play = Button(root,image = playPhoto,command = playMusic)
    stop = Button(root,image = stopPhoto,command = stopMusic)
    pause = Button(root,image = pausePhoto,command = pauseMusic)
    unPause = Button(root,image = playAgainPhoto,command = unpauseMusic)
    next = Button(root,image = nextPhoto,command = nextMusic)
    prev = Button(root,image = prevPhoto,command = prevMusic)

    prev.pack(side = LEFT)
    play.pack(side = LEFT)
    pause.pack(side = LEFT)
    stop.pack(side = LEFT)
    next.pack(side = LEFT)
    unPause.pack(side = RIGHT)

if __name__ == '__main__':
    '''
    Objective           : Main Runner function.
    Input Variables     : None
    Return Value        : None
    Approach            : Invoke the loadMediaPlayer function and mediaPlayerCanvas
                          funtion. 
    '''
    loadMediaPlayer("C:\\Users\\vkjof\Documents\pythonCodesGitHub")
    mediaPlayerCanvas()
    root.mainloop()
