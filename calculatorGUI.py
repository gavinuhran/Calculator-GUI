from tkinter import *
import tkinter.font as font
import math

class Calculator(Frame):
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')
        self.root.geometry("235x320")
        self.root.resizable(0,0)
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        self.createDisplay()
        self.createButtons()

    def createDisplay(self):
        self.displayFont = font.Font(size=40, font="consolas")
        self.textBeingDisplayed = StringVar()
        self.textBeingDisplayed.set('')
        self.totalTextFromUser = ''
        self.display = Label(self.root, textvariable=self.textBeingDisplayed)
        self.display["font"] = self.displayFont
        self.display.grid(row=0, columnspan=4)
    
    def updateDisplay(self, char):
        displayString = ''
        if char == 'CE':
            self.totalTextFromUser = ''
        else:
            self.totalTextFromUser += str(char)
        if len(self.totalTextFromUser) > 25:
            end = len(self.totalTextFromUser)
            start = end - 25
            displayString = self.totalTextFromUser[start:end]
        else:
            displayString = self.totalTextFromUser
        self.textBeingDisplayed.set(displayString)

    def createButtons(self):
        self.myFont = font.Font(size=20)
        self.pixelVirtual = PhotoImage(width=1, height=1)
        self.createOperations()
        self.createDigits()

    def createOperations(self):
        self.operationBGColor = '#84C8FF'
        self.operationFontColor = '#FFFFFF'
        self.createAddButton()
        self.createSubtractButton()
        self.createMultiplyButton()
        self.createDivisionButton()
        self.createSquareRootButton()
        self.createLeftParenthesisButton()
        self.createRightParenthesisButton()
        self.createCalculateButton()
        self.createClearButton()


    def createAddButton(self):
        self.addButton = Button(self.root, text="+", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.addButton["command"] = self.add
        self.addButton["font"] = self.myFont
        self.addButton['bg'] = self.operationBGColor
        self.addButton['fg'] = '#FFFFFF'
        self.addButton.grid(row=5, column=3)

    def add(self):
        self.updateDisplay('+')

    def createSubtractButton(self):
        self.subtractButton = Button(self.root, text="-", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.subtractButton["command"] = self.subtract
        self.subtractButton["font"] = self.myFont
        self.subtractButton['bg'] = self.operationBGColor
        self.subtractButton['fg'] = '#FFFFFF'
        self.subtractButton.grid(row=4, column=3)

    def subtract(self):
        self.updateDisplay('-')

    def createMultiplyButton(self):
        self.multiplyButton = Button(self.root, text="x", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.multiplyButton["command"] = self.multiply
        self.multiplyButton["font"] = self.myFont
        self.multiplyButton['bg'] = self.operationBGColor
        self.multiplyButton['fg'] = '#FFFFFF'
        self.multiplyButton.grid(row=3, column=3)

    def multiply(self):
        self.updateDisplay('*')

    def createDivisionButton(self):
        self.divisionButton = Button(self.root, text="÷", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.divisionButton["command"] = self.divide
        self.divisionButton["font"] = self.myFont
        self.divisionButton['bg'] = self.operationBGColor
        self.divisionButton['fg'] = '#FFFFFF'
        self.divisionButton.grid(row=2, column=3)

    def divide(self):
        self.updateDisplay('/')

    def createSquareRootButton(self):
        self.squareRootButton = Button(self.root, text="√", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.squareRootButton["command"] = self.squareRoot
        self.squareRootButton["font"] = self.myFont
        self.squareRootButton['bg'] = self.operationBGColor
        self.squareRootButton['fg'] = '#FFFFFF'
        self.squareRootButton.grid(row=1, column=2)

    def squareRoot(self):
        if self.totalTextFromUser.replace('.', '', 1).isdigit():
            output = '{:.6f}'.format(math.sqrt(float(self.totalTextFromUser)))
        else:
            output = 'ERROR'
        self.updateDisplay('CE')
        self.updateDisplay(output)

    def createLeftParenthesisButton(self):
        self.leftParenthesisButton = Button(self.root, text="(", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.leftParenthesisButton["command"] = self.leftParenthesis
        self.leftParenthesisButton["font"] = self.myFont
        self.leftParenthesisButton['bg'] = self.operationBGColor
        self.leftParenthesisButton['fg'] = '#FFFFFF'
        self.leftParenthesisButton.grid(row=1, column=0)

    def leftParenthesis(self):
        self.updateDisplay('(')

    def createRightParenthesisButton(self):
        self.rightParenthesisButton = Button(self.root, text=")", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.rightParenthesisButton["command"] = self.rightParenthesis
        self.rightParenthesisButton["font"] = self.myFont
        self.rightParenthesisButton['bg'] = self.operationBGColor
        self.rightParenthesisButton['fg'] = '#FFFFFF'
        self.rightParenthesisButton.grid(row=1, column=1)

    def rightParenthesis(self):
        self.updateDisplay(')')

    def createClearButton(self):
        self.clearButton = Button(self.root, text="CE", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.clearButton["command"] = self.clear
        self.clearButton["font"] = self.myFont
        self.clearButton["bg"] = '#FF7575'
        self.clearButton['fg'] = '#FFFFFF'
        self.clearButton.grid(row=1, column=3)

    def clear(self):
        self.updateDisplay('CE')

    def createCalculateButton(self):
        self.calculateButton = Button(self.root, text="=", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.calculateButton["command"] = self.calculate
        self.calculateButton["font"] = self.myFont
        self.calculateButton["bg"] = '#FF7575'
        self.calculateButton['fg'] = '#FFFFFF'
        self.calculateButton.grid(row=5, column=2)

    def calculate(self):
        response = self.calculateProcess(self.totalTextFromUser)
        self.updateDisplay('CE')
        self.updateDisplay(response)

    def calculateProcess(self, userString):
        userInput = self.stripOuterParenthesis(userString)
        operationIndex = self.findOperation(userInput)
        if not self.checkIfNum(operationIndex):
            return 'ERROR'
        else:
            operation = userInput[operationIndex]

            leftSide = self.stripOuterParenthesis(userInput[:operationIndex])
            rightSide = self.stripOuterParenthesis(userInput[operationIndex+1:])

            if not self.checkIfNum(leftSide):
                leftSide = self.calculateProcess(leftSide)

            if not self.checkIfNum(rightSide):
                rightSide = self.calculateProcess(rightSide)

            leftSide = float(leftSide)
            rightSide = float(rightSide)

            return self.performOperation(leftSide, rightSide, operation)

    def checkIfOuterParenthesis(self, userInput):
        firstCharIsParenthesis = userInput[0] == '('
        numOpenParenthesis = 0
        for i in range(len(userInput)-1):
            char = userInput[i]
            if char ==')' and numOpenParenthesis == 1:
                return False
            elif char == '(':
                numOpenParenthesis += 1
            elif char == ')':
                numOpenParenthesis -= 1
        lastCharIsParenthesis = userInput[len(userInput)-1] == ')'
        return (firstCharIsParenthesis) and (numOpenParenthesis == 1) and (lastCharIsParenthesis)

    def findOperation(self, userInput):
        for iteration in range(2):
            numOpenParenthesis = 0
            for i in range(len(userInput)):
                char = userInput[i]
                if char == '(':
                    numOpenParenthesis += 1
                elif char == ')':
                    numOpenParenthesis -= 1
                else:
                    if (char == '+' or char == '-') and iteration == 0 and numOpenParenthesis == 0:
                        return i
                    if (char == '*' or char == '-') and iteration == 1 and numOpenParenthesis == 0:
                        return i

    def checkIfNum(self, userInput):
        return str(userInput).replace('.', '', 1).isdigit()

    def stripOuterParenthesis(self, userInput):
        if self.checkIfOuterParenthesis(userInput):
            return userInput[1:len(userInput)-1]
        else:
            return userInput

    def performOperation(self, leftSide, rightSide, operation):
        if operation == '+':
            return leftSide + rightSide
        elif operation == '-':
            return leftSide - rightSide
        elif operation == '*':
            return leftSide * rightSide
        else:
            return leftSide / rightSide

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
        self.zeroButton = Button(self.root, text="0", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.zeroButton["command"] = self.addZero
        self.zeroButton["font"] = self.myFont
        self.zeroButton.grid(row=5, column=0)

    def addZero(self):
        self.updateDisplay('0')

    def createOneButton(self):
        self.oneButton = Button(self.root, text="1", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.oneButton["command"] = self.addOne
        self.oneButton["font"] = self.myFont
        self.oneButton.grid(row=4, column=0)

    def addOne(self):
        self.updateDisplay('1')

    def createTwoButton(self):
        self.twoButton = Button(self.root, text="2", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.twoButton["command"] = self.addTwo
        self.twoButton["font"] = self.myFont
        self.twoButton.grid(row=4, column=1)

    def addTwo(self):
        self.updateDisplay('2')

    def createThreeButton(self):
        self.threeButton = Button(self.root, text="3", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.threeButton["command"] = self.addThree
        self.threeButton["font"] = self.myFont
        self.threeButton.grid(row=4, column=2)

    def addThree(self):
        self.updateDisplay('3')

    def createFourButton(self):
        self.fourButton = Button(self.root, text="4", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.fourButton["command"] = self.addFour
        self.fourButton["font"] = self.myFont
        self.fourButton.grid(row=3, column=0)

    def addFour(self):
        self.updateDisplay('4')

    def createFiveButton(self):
        self.fiveButton = Button(self.root, text="5", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.fiveButton["command"] = self.addFive
        self.fiveButton["font"] = self.myFont
        self.fiveButton.grid(row=3, column=1)

    def addFive(self):
        self.updateDisplay('5')

    def createSixButton(self):
        self.sixButton = Button(self.root, text="6", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.sixButton["command"] = self.addSix
        self.sixButton["font"] = self.myFont
        self.sixButton.grid(row=3, column=2)

    def addSix(self):
        self.updateDisplay('6')

    def createSevenButton(self):
        self.sevenButton = Button(self.root, text="7", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.sevenButton["command"] = self.addSeven
        self.sevenButton["font"] = self.myFont
        self.sevenButton.grid(row=2, column=0)

    def addSeven(self):
        self.updateDisplay('7')

    def createEightButton(self):
        self.eightButton = Button(self.root, text="8", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.eightButton["command"] = self.addEight
        self.eightButton["font"] = self.myFont
        self.eightButton.grid(row=2, column=1)

    def addEight(self):
        self.updateDisplay('8')

    def createNineButton(self):
        self.nineButton = Button(self.root, text="9", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.nineButton["command"] = self.addNine
        self.nineButton["font"] = self.myFont
        self.nineButton.grid(row=2, column=2)

    def addNine(self):
        self.updateDisplay('9')

    def createDecimalButton(self):
        self.decimalButton = Button(self.root, text=".", image=self.pixelVirtual, width=51, height=51, compound="c")
        self.decimalButton["command"] = self.addDecimal
        self.decimalButton["font"] = self.myFont
        self.decimalButton.grid(row=5, column=1)

    def addDecimal(self):
        self.updateDisplay('.')

app=Calculator()