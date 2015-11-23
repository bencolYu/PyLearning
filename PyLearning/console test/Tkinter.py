


"""

import tkinter
top = tkinter.Tk()
label=tkinter.Label(top,text="abcdef")
label.pack()
tkinter.mainloop()

"""

'''
from tkinter import *
root= Tk()

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame,text="botton1",fg="red")
button2=Button(topFrame,text="botton2",fg="blue")
button3=Button(topFrame,text="botton3",fg="green")
button4=Button(bottomFrame,text="botton4",fg="purple")

button1.pack(side=LEFT)
button2.pack()
button3.pack()
button4.pack()
'''
'''
def printName(event):
    print("yzz")

def leftClick(event):
    print("left")

def middleClick(event):
    print("middle")

def rightClick(evnet):
    print("right")
'''

'''
label1=Label(root,text="name")
label2=Label(root,text="Password")
entry1=Entry(root)
entry2=Entry(root)

label1.grid(row=0,sticky=W)
label2.grid(row=1)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

checkb1=Checkbutton(root,text="make sure")
'''
'''
button5=Button(root,text="show name",width=15,height=2)
button5.bind("<Button-1>",leftClick)
button5.bind("<Button-2>",middleClick)
button5.bind("<Button-3>",rightClick)
button5.grid()
'''





"""
import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
"""

'''
from tkinter import *


class ButtonEx1:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.printButton=Button(frame,text="print message",command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton=Button(frame,text="quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Ok, clsaa created")
        

root= Tk()
ex=ButtonEx1(root)       
root.mainloop()
'''

from tkinter import *

def doNothing():
    print("yzz doNothing")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project...",command=doNothing)
subMenu.add_command(label="New...",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=root.destroy)

editMenu=Menu(menu)
menu.add_cascade(label="edit",menu=editMenu)
editMenu.add_command(label="redo",command=doNothing)

root.mainloop()