def calculate(userInput):
    operationIndex = findOperation(userInput)
    operation = userInput[operationIndex]

    leftSide = userInput[:operationIndex]
    rightSide = userInput[operationIndex+1:]

    leftSideIsNum = checkIfNum(leftSide)
    rightSideIsNum = checkIfNum(rightSide)

    if not leftSideIsNum:
        leftSide = stripOuterParenthesis(leftSide)
        leftSide = calculate(leftSide)

    if not rightSideIsNum:
        rightSide = stripOuterParenthesis(rightSide)
        rightSide = calculate(rightSide)

    leftSide = float(leftSide)
    rightSide = float(rightSide)

    return performOperation(leftSide, rightSide, operation)

def findOperation(userInput):
    numOpenParenthesis = 0
    for i in range(len(userInput)):
        char = userInput[i]
        if char == '(':
            numOpenParenthesis += 1
        elif char == ')':
            numOpenParenthesis -= 1
        if (char == '+' or char == '-' or char == '*' or char == '/') and numOpenParenthesis == 0:
            return i

def checkIfNum(userInput):
    return userInput.replace('.', '', 1).isdigit()

def stripOuterParenthesis(userInput):
    firstCharIsParenthesis = userInput[0] == '('
    numOpenParenthesis = 0
    for i in range(len(userInput)-1):
        char = userInput[i]
        if char == '(':
            numOpenParenthesis += 1
        elif char == ')':
            numOpenParenthesis -= 1
    lastCharIsParenthesis = userInput[len(userInput)-1] == ')'
    if (firstCharIsParenthesis) and (numOpenParenthesis == 1) and (lastCharIsParenthesis):
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



userInput = '(3+5)*4+6'
print(calculate(userInput))