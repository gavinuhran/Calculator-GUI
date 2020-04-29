def calculate(userString):
    userInput = stripOuterParenthesis(userString)
    operationIndex = findOperation(userInput)
    if not checkIfNum(operationIndex):
        return 'ERROR'
    else:
        operation = userInput[operationIndex]

        leftSide = stripOuterParenthesis(userInput[:operationIndex])
        rightSide = stripOuterParenthesis(userInput[operationIndex+1:])

        leftSideIsNum = checkIfNum(leftSide)
        rightSideIsNum = checkIfNum(rightSide)

        if not leftSideIsNum:
            leftSide = calculate(leftSide)

        if not rightSideIsNum:
            rightSide = calculate(rightSide)

        leftSide = float(leftSide)
        rightSide = float(rightSide)

        return performOperation(leftSide, rightSide, operation)

def checkIfOuterParenthesis(userInput):
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

def findOperation(userInput):
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
        

def checkIfNum(userInput):
    return str(userInput).replace('.', '', 1).isdigit()

def stripOuterParenthesis(userInput):
    if checkIfOuterParenthesis(userInput):
        return userInput[1:len(userInput)-1]
    else:
        return userInput

def performOperation(leftSide, rightSide, operation):
    if operation == '+':
        return leftSide + rightSide
    elif operation == '-':
        return leftSide - rightSide
    elif operation == '*':
        return leftSide * rightSide
    else:
        return leftSide / rightSide



userInput = '(7)+(3)'
print(calculate(userInput))