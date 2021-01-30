from tkinter import *

root = Tk()

arrColours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

r = 0  # row ref
for c in arrColours:
    # Label(text=c).grid(row=RIDGE, width=15, column=0)
    # Entry(bg=c).grid(row=SUNKEN, zidth=10, column=1)
    Label(text=c).grid(row=r, column=0)
    Entry(bg=c).grid(row=r, column=1)
    r = r+1


# background = bg
# foreground = fg

root.mainloop()
