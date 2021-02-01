import tkinter as tk
import tkinter.ttk as ttk

FIT = (tk.NE, tk.SW)
size = 4


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # config title, size and resizable
        self.master.title('2048')
        self.master.geometry('500x550')
        self.master.resizable(False, False)

        # set frame the only item
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=FIT)

        # creat style
        self.creatStyles()

        # creat sub widgets
        self.createWidgets()

    def creatStyles(self):
        style = ttk.Style()
        style.configure('TLabel',
                        background='#FFFFFF',
                        foreground='#000000',
                        borderwidth='20',
                        bordercolor='#000000',
                        relief='solid',
                        anchor='centre')

    def createWidgets(self):
        # set application's layout
        self.rowconfigure(0, weight=1, uniform='2048')
        self.rowconfigure(1, weight=10, uniform='2048')
        self.columnconfigure(0, weight=1, uniform='2048')

        # set upFrame's layout
        upFrame = ttk.Frame(self)
        upFrame.grid(row=0, column=0, sticky=FIT)

        upFrame.columnconfigure(0, weight=1, uniform='upframe')
        upFrame.columnconfigure(1, weight=4, uniform='upframe')
        upFrame.rowconfigure(0, weight=1, uniform='upframe')

        text = ttk.Label(upFrame, text='Score')
        text.grid(row=0, column=0, sticky=FIT)

        text = ttk.Label(upFrame, text='00000000')
        text.grid(row=0, column=1, sticky=FIT)

        # set lowerFrame's layout
        lowerFrame = ttk.Frame(self)
        lowerFrame.grid(row=1, column=0, sticky=FIT)
        for row in range(size):
            lowerFrame.rowconfigure(row, weight=1, uniform='lowerFrame')

        for column in range(size):
            lowerFrame.columnconfigure(column, weight=1, uniform='lowerFrame')

        # creat children widgets
        for row in range(size):
            for column in range(size):
                label = ttk.Label(lowerFrame)
                label.grid(row=row, column=column, sticky=FIT)
                label['text'] = 'empty'


if __name__ == '__main__':
    app = Application()
    app.mainloop()
