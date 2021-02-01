import tkinter as tk
import tkinter.ttk as ttk

# sticky = whole subwidget
FIT = (tk.NE, tk.SW)


class TkinterPortfolio(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # config title, size and resizable
        self.master.title('Portfolio')
        self.master.geometry('500x500')
        self.master.resizable(True, True)

        # set frame the only item
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=FIT)

        # set frame row & column
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # creat sub widgets
        self.createWidgets()

    def createWidgets(self):
        self.leftFrame = ttk.Frame(self)
        self.leftFrame.grid(row=0, column=0, sticky=FIT)
        self.leftFrame.rowconfigure(0, weight=1)
        self.leftFrame.columnconfigure(0, weight=1)
        button = ttk.Button(self.leftFrame)
        button.grid(row=0, column=0, sticky=FIT)
        button['text'] = 'hello'

        self.rightFrame = ttk.Frame(self)
        self.rightFrame.grid(row=0, column=1, sticky=FIT)
        self.rightFrame.rowconfigure(0, weight=1)
        self.rightFrame.columnconfigure(0, weight=1)
        button = ttk.Button(self.rightFrame)
        button.grid(row=0, column=0, sticky=FIT)
        button['text'] = 'world'


# run the program
if __name__ == '__main__':
    folio = TkinterPortfolio()

    folio.mainloop()
