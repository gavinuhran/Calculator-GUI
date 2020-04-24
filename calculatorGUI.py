from tkinter import *

class Calculator(Frame):
    def __init__(self):
        self.root = Tk()
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        self.createDisplay()
        self.createButtons()

    def createDisplay(self):
        self.textBeingDisplayed = StringVar()
        self.textBeingDisplayed.set('')
        self.display = Label(self.root, textvariable=self.textBeingDisplayed)
        self.display.grid(row=0, column=0)

    def createButtons(self):
        self.pixelVirtual = PhotoImage(width=1, height=1)
        self.createOperations()
        self.createDigits()

    def createOperations(self):
        self.createAddButton()
        self.createSubtractButton()
        self.createMultiplyButton()
        self.createDivisionButton()
        self.createCalculateButton()

    def createAddButton(self):
        self.addButton = Button(self.root, text="+", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.addButton["command"] = self.add
        self.addButton.grid(row=4, column=3)

    def add(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '+')

    def createSubtractButton(self):
        self.subtractButton = Button(self.root, text="-", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.subtractButton["command"] = self.subtract
        self.subtractButton.grid(row=3, column=3)

    def subtract(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '-')

    def createMultiplyButton(self):
        self.multiplyButton = Button(self.root, text="x", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.multiplyButton["command"] = self.multiply
        self.multiplyButton.grid(row=2, column=3)

    def multiply(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '*')

    def createDivisionButton(self):
        self.divisionButton = Button(self.root, text="÷", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.divisionButton["command"] = self.divide
        self.divisionButton.grid(row=1, column=3)

    def divide(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '/')

    def createCalculateButton(self):
        self.Button = Button(self.root, text="=", image=self.pixelVirtual, width=30, height=30, compound="c")
        #self.Button["command"] = self.calculate
        self.Button.grid(row=4, column=2)

    def createDigits(self):
        self.createZeroButton()
        self.createOneButton()
        self.createTwoButton()
        self.createThreeButton()
        self.createFourButton()
        self.createFiveButton()
        self.createSixButton()
        self.createSevenButton()
        self.createEightButton()
        self.createNineButton()
        self.createDecimalButton()

    def createZeroButton(self):
        self.ZeroButton = Button(self.root, text="0", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.ZeroButton["command"] = self.addZero
        self.ZeroButton.grid(row=4, column=0)

    def addZero(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '0')

    def createOneButton(self):
        self.oneButton = Button(self.root, text="1", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.oneButton["command"] = self.addOne
        self.oneButton.grid(row=3, column=0)

    def addOne(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '1')

    def createTwoButton(self):
        self.twoButton = Button(self.root, text="2", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.twoButton["command"] = self.addTwo
        self.twoButton.grid(row=3, column=1)

    def addTwo(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '2')

    def createThreeButton(self):
        self.threeButton = Button(self.root, text="3", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.threeButton["command"] = self.addThree
        self.threeButton.grid(row=3, column=2)

    def addThree(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '3')

    def createFourButton(self):
        self.fourButton = Button(self.root, text="4", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.fourButton["command"] = self.addFour
        self.fourButton.grid(row=2, column=0)

    def addFour(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '4')

    def createFiveButton(self):
        self.fiveButton = Button(self.root, text="5", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.fiveButton["command"] = self.addFive
        self.fiveButton.grid(row=2, column=1)

    def addFive(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '5')

    def createSixButton(self):
        self.sixButton = Button(self.root, text="6", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.sixButton["command"] = self.addSix
        self.sixButton.grid(row=2, column=2)

    def addSix(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '6')

    def createSevenButton(self):
        self.sevenButton = Button(self.root, text="7", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.sevenButton["command"] = self.addSeven
        self.sevenButton.grid(row=1, column=0)

    def addSeven(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '7')

    def createEightButton(self):
        self.eightButton = Button(self.root, text="8", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.eightButton["command"] = self.addEight
        self.eightButton.grid(row=1, column=1)

    def addEight(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '8')

    def createNineButton(self):
        self.nineButton = Button(self.root, text="9", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.nineButton["command"] = self.addNine
        self.nineButton.grid(row=1, column=2)

    def addNine(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '9')

    def createDecimalButton(self):
        self.decimalButton = Button(self.root, text=".", image=self.pixelVirtual, width=30, height=30, compound="c")
        self.decimalButton["command"] = self.addDecimal
        self.decimalButton.grid(row=4, column=1)

    def addDecimal(self):
        self.textBeingDisplayed.set(self.textBeingDisplayed.get() + '.')


    # CALCULATE BUTTON DOES NOT HAVE A FUNCTION CALL

app=Calculator()