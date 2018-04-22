'''
Program         : Stop and Wait Protocol
'''

# Importing necessary libraries
from tkinter import *
from random import *
import time

# -----------------------------------------------------------------------------
'''
Creating the canvas for the graphical user interface.

Module Used : Tkinter for GUI
'''
root = Tk()
root.title('Stop and Wait')
canvas = Canvas(root, width=900, height=500)
canvas.pack()
canvas.create_text(100, 50, text="Sender", font="Times 20 italic bold")
canvas.create_text(800, 50, text="Receiver", font="Times 20 italic bold")
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions Definitions
def sender_network():
    '''
    Sender at network layer.

    Parameters
    ----------
    None

    Returns
    -------
    frame : dtype - list, data to be sent to receiver.

    Description
    -----------
    sender_network function definition.

    Approach
    --------
    Defines a list containing the data values to be sent to receiver.
    '''
    frame = [0x1,0x2,0x3,0x4,0x5]
    return frame


def sender_physical(counter):
    '''
    Sender at physical layer.

    Parameters
    ----------
    counter : dtype - int, value of the counter.

    Returns
    -------
    counter : dtype - int, value of the counter after moving the frame.

    Description
    -----------
    sender_physical function description.

    Approach
    --------
    A frame is made and a random number is being generated. According to the
    value of random number, the cases are handled, if frame is going to be
    lost or to be sent successfully to receiver side.
    '''
    frame = draw_frame()
    random = randint(1, 4)
    #print('Sender random', random)
    if (random == 3):
        time.sleep(0.5)
        frame_lost(frame, counter)
        print('Frame lost, sending same again...')
        sender_physical(0)
    else:
        counter = move_frame(frame, counter)
        receiver(frame)
    return int(counter)


def frame_lost(frame, counter):
    '''
    Frame is being lost.

    Parameters
    ----------
    frame : dtype - canvas object, a rectangular frame.
    counter : dtype - int, value of the counter.

    Returns
    -------
    None

    Description
    -----------
    frame_lost function description.

    Approach
    --------
    Frame is being deleted using delete() method of canvas module.
    '''
    time.sleep(5)
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            # print("counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        canvas.move(frame, 5, 0)
        canvas.update()
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            # print("counter: ", counter)
            canvas.update()
        time.sleep(0.25)
    lost = canvas.create_text(450, 250, text="Frame is lost and timeout...", font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    canvas.delete(lost)
    canvas.delete(frame)
    print('Frame is lost...')
    return


def receiver(frame):
    '''
    Receiver Side working.

    Parameters
    ----------
    frame : dtype - canvas object, a rectangular frame.

    Returns
    -------
    None

    Description
    -----------
    receiver function description.

    Approach
    --------
    Notification about the frame being received at receiver side.
    '''
    framereceived = canvas.create_text(450, 250, text="Frame Received.", font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    canvas.delete(framereceived)
    canvas.delete(frame)
    print('Data received at physical layer of receiver...')
    return


def acknowledgement_received(ack, counter):
    '''
    Acknowledgement being received at sender side and new frame is ready
    to be sent.

    Parameters
    ----------
    ack : dtype - canvas object, acknowledgement.
    counter : dtype - int, value of the counter.

    Returns
    -------
    None

    Description
    -----------
    acknowledgement_received function description.

    Approach
    --------
    A notification about the acknowledgement being received at sender side
    and telling the sender to send the next frame to the receiver.
    '''
    move_ack(ack, counter)
    ackrec = canvas.create_text(450, 250, text="Ack Received. Ready for next frame.", font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    canvas.delete(ack)
    canvas.delete(ackrec)
    print('Acknowledgement received.')
    return


def acknowledgement_lost(ack, counter):
    '''
    Acknowledgement being lost while moving from receiver to sender side.

    Parameters
    ----------
    ack : dtype - canvas object, acknowledgement.
    counter : dtype - int, value of the counter.

    Returns
    -------
    None

    Description
    -----------
    acknowledgement_lost function description.

    Approach
    --------
    A notification about the acknowledgement being lost while going from receiver
     side to sender's side.
    '''
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            canvas.update()
        time.sleep(0.25)
        canvas.move(ack, -7, 0)
        canvas.update()
    acklost = canvas.create_text(450, 250, text="Time out...! Acknowledge Lost, send the same frame again", font="Times 15 italic bold")
    canvas.update()
    time.sleep(1)
    canvas.delete(acklost)
    canvas.delete(ack)
    print('Acknowledgement lost.')
    return

def wait_for_event(counter):
    '''
    main function whihc functions the stop and wait protocol.

    Parameters
    ----------
    counter : dtype - int, value of the counter.

    Returns
    -------
    None

    Description
    -----------
    wait_for_event function description.

    Approach
    --------
    Data from sender_network helper function is assigned to a variable.
    Usinga for loop, the frames are being sent one by one. A random function is
    used to randomly deletes an acknowledgement.
    '''
    data = sender_network()
    for i in data:
        counter = int(sender_physical(0))
        #print("Counter value in wait for event", counter)
        random = randint(1, 4)
        ack = draw_ack()
        if (random == 3):
            time.sleep(0.25)
            acknowledgement_lost(ack, counter)
            print('Sending same frame again...')
            counter = int(sender_physical(0))
            ack = draw_ack()
            acknowledgement_received(ack, counter)
        else:
            acknowledgement_received(ack, counter)


def draw_frame():
    '''
    Drawing a rectangular frame to show the data packet.

    Parameters
    ----------
    None

    Returns
    -------
    dtype - canvas object,a rectangle which is used to display the data packet.

    Description
    -----------
    draw_frame function description.

    Approach
    --------
    member function of canvas module is used to draw a rectangle.
    '''
    return canvas.create_rectangle(50, 100, 120, 150, fill='green')


def move_frame(frame, counter):
    '''
    Move a frame.

    Parameters
    ----------
    frame : dtype - canvas object, frame.
    counter : dtype - int, value of the counter.

    Returns
    -------
    counter : dtype - int, value of the counter.

    Description
    -----------
    move_frame function description.

    Approach
    --------
    canvas.move method is used to move the frame. The canvas is needed to be
    updated so that we get to see the latest frame on new location. A timer
    is also being maintained for the protocol timer.
    '''
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            #print("Counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        canvas.move(frame, 30, 0)
        canvas.update()
    return counter


def draw_ack():
    '''
    Draw acknowledgement frame.

    Parameters
    ----------
    None

    Returns
    -------
    A frame, dtype - canvas object, for the acknowledgement purpose.

    Description
    -----------
    draw_ack function description.

    Approach
    --------
    canvas.crate_rectangle method is used to create an acknowledgement frame.
    '''
    return canvas.create_rectangle(700, 100, 780, 150, fill='red')


def move_ack(ack, counter):
    '''
    Move an acknowledgement frame.

    Parameters
    ----------
    ack : dtype - canvas object, acknowledgement.
    counter : dtype - int, value of the counter.

    Returns
    -------
    counter : dtype - int, value of the counter.

    Description
    -----------
    move_ack function description.

    Approach
    --------
    canvas.move method is used to move the acknowledgement frame. The canvas is
    needed to be updated so that we get to see the latest frame on new location.
    A timer is also being maintained for the protocol timer.
    '''
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            #print("Counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        canvas.move(ack, -28, 0)
        canvas.update()
    return counter

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Main handler block
counter = 0
timer = canvas.create_text(450, 450, text="Timer", font="Times 30 italic bold")
wait_for_event(counter)
root.mainloop()
# -----------------------------------------------------------------------------
