from tkinter import *
master = Tk()

text = """
If tkinter is 8.5 or above you'll want the selection background to appear like it does when the widget is activated. Comment this out for older versions of Tkinter.

This is even more text.

The final line of our auto-wrapping label that supports clipboard copy.
""".strip()

frameLabel = Frame(master, padx=20, pady=20)
frameLabel.pack()
w = Text(frameLabel, wrap='word', font='Arial 12 italic')
w.insert(1.0, END)
w.delete(1.0, END)
w.pack()

# - have selection background appear like it does when the widget is activated (Tkinter 8.5+)
# - have label background color match its parent background color via .cget('bg')
# - set relief='flat' to hide Text control borders
# - set state='disabled' to block changes to text (while still allowing selection/clipboard copy)
w.configure(bg=master.cget('bg'), relief='flat', state='disabled')

mainloop()
