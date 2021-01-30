import tkinter as tk
import tkinter as ttk


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # config title, size and resizable
        self.master.title('2048')
        self.master.geometry('300x300')
        self.master.resizable(False, False)

        # set frame the only item
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.NE + tk.SW)

        # creat sub widgets
        self.createWidgets()

    def createWidgets(self):
        pass


if __name__ == '__main__':
    app = Application()
    app.mainloop()
