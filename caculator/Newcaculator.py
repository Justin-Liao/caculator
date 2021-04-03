import tkinter as tk
import tkinter.ttk as ttk

FULL = (tk.NE, tk.SW)


class MachineState():
    def __init__(self, pattern, action, newState):
        self.pattern = pattern
        self.action = action
        self.newState = newState


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # config title, size and resizable
        self.master.title('caculator')
        self.master.geometry('300x350')
        self.master.resizable(False, False)

        # set frame the only item
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=FULL)

        # set frame row & column
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)
        self.columnconfigure(0, weight=1)

        # creat sub widgets
        self.createWidgets()

        style = ttk.Style()
        style.configure('TButton', font=('calabri', 20))

        # caculator state
        self.machine = {
            'Number': (
                MachineState('0123456789', self.numberNumber, 'Number'),
                MachineState('+-x/', self.numberOp, 'Operator'),
                MachineState('=', self.none, 'Number'),
                MachineState('c', self.clear, 'Number')
            ),
            'Operator': (
                MachineState('0123456789', self.opNumber, 'Number2'),
                MachineState('+-x/', self.opOp, 'Operator'),
                MachineState('=', self.opEqual, 'Result'),
                MachineState('c', self.clear, 'Number')
            ),
            'Number2': (
                MachineState('0123456789', self.number2Number, 'Number2'),
                MachineState('+-x/', self.number2Op, 'Operator'),
                MachineState('=', self.number2Equal, 'Result'),
                MachineState('c', self.clear, 'Number')
            ),
            'Result': (
                MachineState('0123456789', self.resultNumber, 'Number'),
                MachineState('+-x/', self.resultOp, 'Operator'),
                MachineState('=', self.resultEqual, 'Result'),
                MachineState('c', self.clear, 'Number')
            )
        }
        self.stateName = 'Number'
        self.state = self.machine['Number']
        self.clear(None)

    def inputEvent(self, inputVal):
        for action in self.state:
            if inputVal in action.pattern:
                action.action(inputVal)
                self.stateName = action.newState
                self.state = self.machine[action.newState]
                return

    def numberNumber(self, inputVal):
        self.currentVal = self.currentVal*10+int(inputVal)

    def numberOp(self, inputVal):
        self.op = inputVal
        self.firstVal = self.currentVal

    def opOp(self, inputVal):
        self.op = inputVal

    def opNumber(self, inputVal):
        self.currentVal = int(inputVal)

    def opEqual(self, inputVal):
        self.currentVal = self.calOp(self.firstVal, self.op, self.firstVal)

    def number2Number(self, inputVal):
        self.currentVal = self.currentVal*10+int(inputVal)

    def number2Op(self, inputVal):
        self.currentVal = self.calOp(self.firstVal, self.op, self.currentVal)
        self.op = inputVal
        self.firstVal = self.currentVal

    def number2Equal(self, inputVal):
        self.currentVal = self.calOp(self.firstVal, self.op, self.currentVal)

    def resultNumber(self, inputVal):
        self.currentVal = int(inputVal)

    def resultOp(self, inputVal):
        self.op = inputVal
        self.firstVal = self.currentVal

    def resultEqual(self, inputVal):
        self.none(inputVal)

    def clear(self, inputVal):
        self.op = ''
        self.firstVal = 0
        self.currentVal = 0

    def none(self, inputVal):
        pass

    def calOp(self, firstVal, op, currentVal):
        if op == '+':
            currentVal = firstVal + currentVal
        elif op == '-':
            currentVal = firstVal - currentVal
        elif op == 'x':
            currentVal = firstVal * currentVal
        elif op == '/' and currentVal != 0:
            currentVal = firstVal / currentVal
        else:
            currentVal = 'Error'

        return currentVal

    def inputActionGenerator(self, intputVal):
        def action():
            self.inputEvent(intputVal)
            self.number.set(self.currentVal)
            # the print below is just for testing the programs
            print('state: ' + self.stateName)
            print('firstVal: ' + str(self.firstVal))
            print('op: ' + self.op)
            print('currentVal: ' + str(self.currentVal))

        return action

    def createWidgets(self):
        self.number = tk.StringVar()
        self.number.set('0 ')
        style = ttk.Style()
        style.configure('Input.TLabel', background='#dbdbdb')
        style.configure('KeyPad.TLabel')  # foreground='lightblue'

        self.input = ttk.Entry(self, font=(
            'calabri', 20, 'bold'), textvariable=self.number, justify='right')
        self.input.grid(row=0, column=0, sticky=FULL)
        self.input['style'] = 'Input.TLabel'

        self.keyPad = ttk.Frame(self)
        self.keyPad.grid(row=1, column=0, sticky=FULL)
        self.keyPad['style'] = 'KeyPad.TLabel'

        for row in range(5):
            self.keyPad.rowconfigure(row, weight=1)

        for column in range(4):
            self.keyPad.columnconfigure(column, weight=1)

        # [number, (row, column, rowspan, columnspan)]
        characters = [
            # digits
            ['1', (3, 0, 1, 1)],
            ['2', (3, 1, 1, 1)],
            ['3', (3, 2, 1, 1)],
            ['4', (2, 0, 1, 1)],
            ['5', (2, 1, 1, 1)],
            ['6', (2, 2, 1, 1)],
            ['7', (1, 0, 1, 1)],
            ['8', (1, 1, 1, 1)],
            ['9', (1, 2, 1, 1)],
            ['0', (4, 0, 1, 3)],
            # operator
            ['+', (0, 3, 1, 1)],
            ['-', (1, 3, 1, 1)],
            ['x', (2, 3, 1, 1)],
            ['/', (3, 3, 1, 1)],
            ['=', (4, 3, 1, 1)],
            # c
            ['c', (0, 0, 1, 3)]
        ]

        for char in characters:
            self.btn = ttk.Button(
                self.keyPad, command=self.inputActionGenerator(char[0]))
            self.btn.grid(row=char[1][0], column=char[1][1],
                          rowspan=char[1][2], columnspan=char[1][3], sticky=FULL)
            self.btn['text'] = char[0]


if __name__ == '__main__':
    app = Application()

    app.mainloop()
