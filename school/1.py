from tkinter import *


root = Tk()
#master = Tk()


text1 = Text(root, height=20, width=30)
photo = PhotoImage(file='test.gif')
text1.insert(END, '\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT, fill=Y)

text2 = Text(root, height=20, width=30)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)

text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('color', foreground='#FF0000')  # color = any RGB

text2.tag_bind('follow', '<l>', lambda e, t=text2: t.insert(END, ""))
text2.insert(END, '\nABCD\n', 'bold_italics')
quote = 'DCBA'

text2.insert(END, quote, 'color')
text2.pack(side=LEFT, fill=Y)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
