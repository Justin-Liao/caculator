import tkinter as tk

window = tk.Tk()

window.title("Calculator")
window.geometry("300x300")

rowCount = 4
columnCount = 4

for row in range(rowCount):
    window.rowconfigure(row, weight=1)

for column in range(columnCount):
    window.columnconfigure(column, weight=1)

display = tk.Entry(window)
display.grid(row=0, column=0, columnspan=4, sticky=tk.N + tk.S + tk.E + tk. W)

for row in range(1, rowCount):
    for column in range(columnCount):
        btn = tk.Button(window)
        btn['text'] = (row-1) * 3 + column + 1
        btn.grid(row=row, column=column, sticky=tk.NE + tk.SW)

window.mainloop()
