import tkinter
import tkinter.ttk as ttk

window = tkinter.Tk()

window.title('caculator')
window.geometry('300x300')


lbl = tkinter.Label(window, text="Hello", font=(
    "Arial Bold", 10), bg="black", fg="white")

txt = tkinter.Entry(window)
txt.grid(column=0, row=0, columnspan=3, sticky=(tkinter.W, tkinter.E))


def one():
    res = txt.get()
    lbl.configure(text=res)


num = 0
for row in range(3):
    for column in range(3):
        num += 1
        btn = ttk.Button(window, text=num, command=num)
        btn.grid(row=row+1, column=column, sticky=tkinter.N +
                 tkinter.S + tkinter.E + tkinter. W)


btnOne = ttk.Button(window, text='0', command=one)
btnOne.grid(column=1, row=4)

window.mainloop()
