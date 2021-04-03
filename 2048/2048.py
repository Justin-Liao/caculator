'''
旧版内容（不完整）
def mergeBox(self, line):
    current = 0
    for index in range(len(line)):
        if line[index].value != -1:
            line[current].value = line[index].value
            line[index].value = -1
            current += 1

def compactLeft(self, line):
current = None

for box in line:
    if box.value == -1 and current == None:
        current = box
    elif box.value != -1 and current != None:
        current.value = box.value
        box.value = -1
        current = box

'''

import sys
import random
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as massagebox

FIT = (tk.NE, tk.SW)
# size = int(input("Please input gameboard size:"))
size = 4


class Box:
    def __init__(self, value=-1):
        self.value = value
        self.widget = None

    def print(self):
        if (self.widget):
            if (self.value > 0):
                self.widget['text'] = str(self.value)
                self.widget['style'] = str(self.value) + ".TLabel"
            else:
                self.widget['text'] = ""
                self.widget['style'] = "TLabel"

    def setWidget(self, widget):
        self.widget = widget

    # def print(self):
    #     if self.value == -1:
    #         print("      ", end='')
    #     if self.value >= 2:
    #         print("{:5d} ".format(self.value), end='')


class GameBoard:

    def __init__(self, size):
        self.size = size
        self.boxes = []
        self.score = 0

        for _row in range(size):
            row = []
            for _column in range(size):
                box = Box()
                row.append(box)

            self.boxes.append(row)

        # self.boxes[0][0].set(2)

    def print(self):
        for row in range(self.size):
            for column in range(self.size):
                box = self.boxes[row][column]
                box.print()

        # for x in range(self.size):
        #     print('———————' * self.size + '—')
        #     # print('|      ' * self.size + '|') 空行

        #     for y in range(self.size):
        #         print('|', end='')
        #         self.boxes[x][y].print()
        #     print('|')
        #     # print('|      ' * self.size + '|') 空行

        # print('———————' * self.size + '—')

    def randomBox(self):
        empty = []
        inside = [2, 2, 4]
        for a in range(self.size):
            for b in range(self.size):
                if self.boxes[a][b].value == -1:
                    empty.append(self.boxes[a][b])
        if len(empty) > 0:
            x = random.randint(0, (len(empty)-1))
            n = inside[random.randint(0, 2)]
            empty[x].value = n
            self.score += n

    def compactLeft(self, line):
        result = False
        for index in range(self.size-1):
            if line[index].value == -1 and line[index+1].value != -1:
                result = True
        valueList = []
        for box in line:
            if box.value != -1:
                valueList.append(box.value)
                box.value = -1

        for index in range(len(valueList)):
            line[index].value = valueList[index]

        return result

    def mergeLine(self, line):
        result = False
        if self.compactLeft(line):
            result = True

        for index in range(self.size-1):
            if line[index].value == line[index+1].value and line[index].value != -1:
                line[index].value *= 2
                line[index+1].value = -1
                result = True
        if self.compactLeft(line):
            result = True

        return result

    def mergeBoardLeft(self):  # a
        result = False
        for lList in self.boxes:
            if self.mergeLine(lList):
                result = True

        return result

    def mergeBoardRight(self):  # d
        result = False
        for row in range(self.size):
            rList = []
            for column in range(self.size):
                rList.insert(0, self.boxes[row][column])
            if self.mergeLine(rList):
                result = True
        return result

    def mergeBoardDown(self):  # s
        result = False
        for column in range(self.size):
            dList = []
            for row in range(self.size):
                dList.insert(0, self.boxes[row][column])
            if self.mergeLine(dList):
                result = True
        return result

    def mergeBoardUp(self):  # w
        result = False
        for column in range(self.size):
            wList = []
            for row in range(self.size):
                wList.append(self.boxes[row][column])
            if self.mergeLine(wList):
                result = True
        return result

    def detect(self):
        gameover = True
        for box in self.boxes:
            for value in box:
                if value.value == -1:
                    gameover = False
                    return gameover
                elif len(self.boxes) == 1:
                    return gameover

        for row in range(self.size-1):
            for column in range(self.size-1):
                if (self.boxes[row][column].value == self.boxes[row][column+1].value
                        or self.boxes[row][column].value == self.boxes[row+1][column].value):
                    gameover = False
                    return gameover
        if (self.boxes[self.size-1][self.size-2].value == self.boxes[self.size-1][self.size-1].value
                or self.boxes[self.size-2][self.size-1].value == self.boxes[self.size-1][self.size-1].value):
            gameover = False
            return gameover
        return gameover

    def compact(self):
        if self.detect():
            self.randomBox()
            self.print()

    def clear(self):
        for row in range(size):
            for column in range(size):
                self.boxes[row][column].value = -1

    def start(self):
        self.clear()
        self.randomBox()
        self.print()
        # self.detect()

        # if self.detect():
        #     pass
        # elif not self.detect():
        #     print("GAME OVER")

        #     print("")
        #     instruction = input(
        #         "a(left), d(right), s(down), w(up)\nPlease input instruction\n:")

        #     # instruction = 'd'
        #     if instruction == 'exit':
        #         break
        #     elif instruction == 'w':  # up
        #         if self.mergeBoardUp():
        #             self.compact()

        #     elif instruction == 'a':  # left
        #         if self.mergeBoardLeft():
        #             self.compact()

        #     elif instruction == 's':  # down
        #         if self.mergeBoardDown():
        #             self.compact()

        #     elif instruction == 'd':  # right
        #         if self.mergeBoardRight():
        #             self.compact()

        #     elif instruction == '':
        #         self.print()
        #     else:
        #         print("instruction wrong")


class Application(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        # config title, size and resizable
        self.master.title('2048')
        self.master.geometry('500x550')
        self.master.resizable(False, False)

        # set master 1x1
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        # set my self into parent's cell
        self.grid(row=0, column=0, sticky=FIT)

        # set size
        self.gameBoard = GameBoard(size)

        # creat style
        self.creatStyles()

        # creat sub widgets
        self.createWidgets()

        # bind the key press event
        self.bind_all('<Key>', self.keypressHandler)

        self.gameBoard.start()

    def creatStyles(self):
        style = ttk.Style()
        style.configure('TLabel',
                        background='#FFFFFF',
                        foreground='#000000',
                        bordercolor='#000000',
                        borderwidth='20',
                        relief='solid',
                        anchor='centre',
                        font='Helvetica 25')
        style.configure("2.TLabel", background="khaki1")
        style.configure("4.TLabel", background="khaki2")
        style.configure("8.TLabel", background="LightPink1")
        style.configure("16.TLabel", background="SeaGreen1")
        style.configure("32.TLabel", background="lightBlue1")
        style.configure("64.TLabel", background="lavender")
        style.configure("128.TLabel", background="LightYellow2")
        style.configure("256.TLabel", background="bisque1")
        style.configure("512.TLabel", background="bisque2")
        style.configure("1024.TLabel", background="bisque3")
        style.configure("2048.TLabel", background="bisque4")

    def createWidgets(self):
        # set application's layout
        self.rowconfigure(0, weight=1, uniform='2048')
        self.rowconfigure(1, weight=10, uniform='2048')
        self.columnconfigure(0, weight=1, uniform='2048')

        # set upFrame's layout
        upFrame = ttk.Frame(self)
        upFrame.grid(row=0, column=0, sticky=FIT)

        upFrame.columnconfigure(0, weight=1, uniform='upframe')
        upFrame.columnconfigure(1, weight=3, uniform='upframe')
        upFrame.columnconfigure(2, weight=1, uniform='upframe')
        upFrame.rowconfigure(0, weight=1, uniform='upframe')

        text = ttk.Label(upFrame, text='Score')
        text.grid(row=0, column=0, sticky=FIT)

        text = ttk.Label(upFrame, text=str(self.gameBoard.score))
        text.grid(row=0, column=1, sticky=FIT)

        self.restart = tk.Button(upFrame, command=self.NewGame)
        self.restart.grid(row=0, column=2, sticky=FIT)
        self.restart['text'] = 'NewGame'
        self.restart['font'] = 'Helvetica 15'

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

                self.gameBoard.boxes[row][column].setWidget(label)

    def NewGame(self):
        self.gameBoard.start()
        # app = Application()
        # app.mainloop()

    def keypressHandler(self, event):
        move = False
        if (event.keysym == 'Left' or event.keysym == 'a'):
            move = self.gameBoard.mergeBoardLeft()
        elif (event.keysym == 'Right' or event.keysym == 'd'):
            move = self.gameBoard.mergeBoardRight()
        elif (event.keysym == 'Up' or event.keysym == 'w'):
            move = self.gameBoard.mergeBoardUp()
        elif (event.keysym == 'Down' or event.keysym == 's'):
            move = self.gameBoard.mergeBoardDown()
        if move:
            self.gameBoard.randomBox()
            self.gameBoard.print()
            print(event.keysym)
        if self.gameBoard.detect():
            if tk.messagebox.askokcancel(
                    title='Gameover', message='Game Over'):
                self.NewGame()
            else:
                pass


if __name__ == '__main__':
    app = Application()
    app.mainloop()


# Board = GameBoard(size)
# Board.start()
