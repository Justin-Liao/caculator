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


class Box:
    def __init__(self, value=-1):
        self.value = value

    def print(self):
        if self.value == -1:
            print("      ", end='')
        if self.value >= 2:
            print("{:5d} ".format(self.value), end='')


class GameBoard:

    def __init__(self, size):
        self.size = size
        self.boxes = []

        for _row in range(size):
            row = []
            for _column in range(size):
                box = Box()
                row.append(box)

            self.boxes.append(row)

        # self.boxes[0][0].set(2)

    def print(self):
        for x in range(self.size):
            print('———————' * self.size + '—')
            # print('|      ' * self.size + '|') 空行

            for y in range(self.size):
                print('|', end='')
                self.boxes[x][y].print()
            print('|')
            # print('|      ' * self.size + '|') 空行

        print('———————' * self.size + '—')

    def randomBox(self):
        empty = []
        for a in range(self.size):
            for b in range(self.size):
                if self.boxes[a][b].value == -1:
                    empty.append(self.boxes[a][b])
        if len(empty) > 0:
            x = random.randint(0, (len(empty)-1))
            empty[x].value = 2

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
        game = False
        for box in self.boxes:
            for value in box:
                if value.value == -1:
                    game = True
                    return game
                elif len(self.boxes) == 1:
                    return game

        for row in range(self.size-1):
            for column in range(self.size-1):
                if (self.boxes[row][column].value == self.boxes[row][column+1].value
                        or self.boxes[row][column].value == self.boxes[row+1][column].value):
                    game = True
                    return game
        return game

    def compact(self):
        if self.detect():
            self.randomBox()
            self.print()

    def start(self):
        self.randomBox()
        self.print()
        self.detect()

        while True:

            if not self.detect():
                print("GAME OVER")
                break

            print("")
            instruction = input(
                "a(left), d(right), s(down), w(up)\nPlease input instruction\n:")

            # instruction = 'd'
            if instruction == 'exit':
                break
            elif instruction == 'w':  # up
                if self.mergeBoardUp():
                    self.compact()

            elif instruction == 'a':  # left
                if self.mergeBoardLeft():
                    self.compact()

            elif instruction == 's':  # down
                if self.mergeBoardDown():
                    self.compact()

            elif instruction == 'd':  # right
                if self.mergeBoardRight():
                    self.compact()

            elif instruction == '':
                self.print()
            else:
                print("instruction wrong")


# boardSize = int(input("Please input gameboard size:"))
boardSize = 4

Board = GameBoard(boardSize)

Board.start()
# Board.detect()
