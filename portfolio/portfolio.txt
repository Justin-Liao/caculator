import os
import tkinter as tk
import tkinter.ttk as ttk


FIT = (tk.NE, tk.SW)
DIR = os.path.dirname(os.path.abspath(__file__))


class TkinterPortfolio(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # config title, size and resizable
        self.master.title('Portfolio')
        self.master.geometry('600x500')
        self.master.resizable(False, False)

        # set frame the only item
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=FIT)

        # set frame row & column
        self.columnconfigure(0, weight=1, uniform="u")
        self.columnconfigure(1, weight=1, uniform="u")
        self.rowconfigure(0, weight=9, uniform="u")
        self.rowconfigure(1, weight=1, uniform="u")

        # creat sub widgets
        self.createWidgets()

    def createWidgets(self):
        self.picture = ttk.Label(self)
        self.picture.grid(row=0, column=0, sticky=FIT)

        self.text = ttk.Frame(self, width=10)
        self.text.grid(row=0, column=1, sticky=FIT)
        self.txt = tk.Text(self.text, wrap='word',
                           relief='flat', font='Arial 12 italic')
        self.txt.pack()
        # self.txt.grid(row=0, column=0, sticky=FIT)

        self.downFrame = ttk.Frame(self)
        self.downFrame.grid(row=1, column=0, columnspan=2, sticky=FIT)
        self.downFrame.rowconfigure(0, weight=1)
        self.downFrame.columnconfigure(0, weight=1)
        self.downFrame.columnconfigure(1, weight=1)
        self.downFrame.columnconfigure(2, weight=1)

        btn = ttk.Button(self.downFrame, text='<-', command=self.prevPage)
        btn.grid(row=0, column=0, sticky=FIT)
        btn = ttk.Button(self.downFrame, text='->', command=self.nextPage)
        btn.grid(row=0, column=2, sticky=FIT)

        self.currentPage = 0
        self.pages = tk.StringVar()
        self.pages.set('Page '+str(self.currentPage+1))
        self.midbtn = ttk.Button(
            self.downFrame, textvariable=self.pages, command=self.menu)
        self.midbtn.grid(row=0, column=1, sticky=FIT)

        self.setCurrentContent(self.currentPage)

    def nextPage(self):
        if self.currentPage < 4:
            self.currentPage += 1
            self.setCurrentContent(self.currentPage)
            self.pages.set('Page '+str(self.currentPage+1))

    def prevPage(self):
        if self.currentPage > 0:
            self.currentPage -= 1
            self.setCurrentContent(self.currentPage)
            self.pages.set('Page '+str(self.currentPage+1))

    def menu(self):
        self.destroy()
        text = ttk.Entry()
        text.grid(row=0, column=0)
        text.insert(0, 'thank you for using :)')

    def setCurrentContent(self, index):
        imageFile = DIR + '/' + contentList[index][0]
        text = contentList[index][1]
        self.image = tk.PhotoImage(file=imageFile)
        self.picture['image'] = self.image

        self.txt.configure(state='normal')
        self.txt.delete(1.0, tk.END)
        self.txt.insert(1.0, text)
        self.txt.configure(state='disabled')


text1 = ''' My portfolio explanation\n I used tkinter and tkinter.ttk in this program. I first set the title, widow size and make the window unresiwable. Then i set the row and column by using ttk.frame in this class. I set the master frame as the root frame. I made 2 row and 2 column in master. Then I create the inside widgets, i will show it in the next page. Just click the "->" button at the bottom. \n By the way, the picture is very blury because i resized it. ttk.label does not have zoom or resize option so i have to do it outside. Some program in the picture is different to the one it send to you, it still have some problem when i took a screenshot so the one i send email to you is correct. 
'''
text2 = ''' This picture I was setting my picture and text widgets.\n I used ttk.lable to show my picture and I tried to use ttk.entry to show my text but i finally decided to use the tk.text widget becausethe entry cannot change the size. The button part i made another frame and seperate it in 1 row and 3 column.\n I wanted to show the pages when the middel button was clicked but i do not know how to do that so i changed it into a destory function.
'''
text3 = ''' This page was the command of the button and the text change function.\n The first and the second function was controning the next and previous page. the menu one was delete all the things in the function. ummm... maybe this will make you confused.
'''
text4 = ''' This is where i put the texts and the pictures.
'''
text5 = '''  please press the middle button now. : )'''

contentList = [
    ['image1.png', text1],
    ['image2.png', text2],
    ['image3.png', text3],
    ['image4.png', text4],
    ['image5.png', text5],
]


# run the program
if __name__ == '__main__':
    folio = TkinterPortfolio()

    folio.mainloop()
