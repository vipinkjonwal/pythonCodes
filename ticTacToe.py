from tkinter import *
import tkinter.messagebox
tk = Tk()
#tk is object of Tk() module.

tk.title("TIC TAC TOE")
#title() is used to set the title of application.

click = True

def inputValues(buttons):
    global click
    if (buttons["text"] == " ") and (click == True):
        buttons["text"] = "x"
        click = False

    if (buttons["text"] == " ") and (click == False):
        buttons["text"] = "o"
        click = True

    if((button1["text"] == "x" and button2["text"] == "x" and button3["text"] == "x") or
        (button4["text"] == "x" and button5["text"] == "x" and button6["text"] == "x") or
        (button7["text"] == "x" and button8["text"] == "x" and button9["text"] == "x") or
        (button1["text"] == "x" and button4["text"] == "x" and button7["text"] == "x") or
        (button2["text"] == "x" and button5["text"] == "x" and button8["text"] == "x") or
        (button3["text"] == "x" and button6["text"] == "x" and button9["text"] == "x") or
        (button1["text"] == "x" and button5["text"] == "x" and button9["text"] == "x") or
        (button3["text"] == "x" and button5["text"] == "x" and button7["text"] == "x")):
        tkinter.messagebox.showinfo(title = "WINNER", message = "X : You won the Game")

    if ((button1["text"] == "o" and button2["text"] == "o" and button3["text"] == "o") or
        (button4["text"] == "o" and button5["text"] == "o" and button6["text"] == "o") or
        (button7["text"] == "o" and button8["text"] == "o" and button9["text"] == "o") or
        (button1["text"] == "o" and button4["text"] == "o" and button7["text"] == "o") or
        (button2["text"] == "o" and button5["text"] == "o" and button8["text"] == "o") or
        (button3["text"] == "o" and button6["text"] == "o" and button9["text"] == "o") or
        (button1["text"] == "o" and button5["text"] == "o" and button9["text"] == "o") or
        (button3["text"] == "o" and button5["text"] == "o" and button7["text"] == "o")):
        tkinter.messagebox.showinfo(title="WINNER", message="O : You won the Game")

buttons = StringVar()
#StringVar() is used to call the corresponding constructor to create a tkinter variable.

button1 = Button(tk,text = " ",height = 4, width = 8, command = lambda:inputValues(button1))
button1.grid(row = 1, column = 0,sticky = S+N+E+W)
#lambda is used to create anonymous function.
#Anonymous function is a function that is defined without name, created with lambda keyword.

button2 = Button(tk,text = " ",height = 4, width = 8, command = lambda:inputValues(button2))
button2.grid(row = 1, column = 1,sticky = S+N+E+W)

button3 = Button(tk,text = " ",height = 4, width = 8, command = lambda:inputValues(button3))
button3.grid(row = 1, column = 2,sticky = S+N+E+W)

button4 = Button(tk,text = " ",height = 4, width = 8, command = lambda:inputValues(button4))
button4.grid(row = 2, column = 0,sticky = S+N+E+W)

button5 = Button(tk,text = " ",height = 4, width = 8, command = lambda:inputValues(button5))
button5.grid(row = 2, column = 1,sticky = S+N+E+W)

button6 = Button(tk,text = " ",height = 4, width = 8, command = lambda:inputValues(button6))
button6.grid(row = 2, column = 2,sticky = S+N+E+W)

button7 = Button(tk,text = " ",height = 4, width = 8, command = lambda:inputValues(button7))
button7.grid(row = 3, column = 0,sticky = S+N+E+W)

button8 = Button(tk,text = " ",height = 4, width = 8, command = lambda:inputValues(button8))
button8.grid(row = 3, column = 1,sticky = S+N+E+W)

button9 = Button(tk,text = " ",height = 4, width = 8, command = lambda:inputValues(button9))
button9.grid(row = 3, column = 2,sticky = S+N+E+W)

tk.mainloop()
#endOfProgram