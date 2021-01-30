from tkinter import *
import sys


def NewFile():
    print("NewFile")


def OpenFile():
    print("OpenFile")


def Quit():
    sys.exit()


root = Tk()

menu = Menu(root)

root.config(menu=menu)

filemenu = Menu(menu)

filemenu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Quit)

root.mainloop()
