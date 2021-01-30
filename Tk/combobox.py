from tkinter import *

from tkinter import messagebox

from tkinter import Menu

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

menu = Menu(window)

menu.add_command(label='File')

window.config(menu=menu)


def cmd():
    messagebox.showinfo('Message title', combo.get())


btn = Button(window, text="Button", command=cmd)

btn.grid(column=1, row=0)

combo = Combobox(window)

combo['values'] = (1, 2, 3, 4, 5, "Text")

combo.current(5)  # set the selected item

combo.grid(column=0, row=0)

window.mainloop()
