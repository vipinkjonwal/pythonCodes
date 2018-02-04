def postfixEvaluation(givenExpression):

    digits = [str(x) for x in range(10)]
    operations = ['+','-','*','/']
    tempStack = []

    for i in range(len(givenExpression)):
        if givenExpression[i] in digits:
            tempStack.append(int(givenExpression[i]))
        elif givenExpression[i] in operations:
            operand2 = tempStack.pop()
            operand1 = tempStack.pop()

            if givenExpression[i] == '+':
                tempStack.append(operand1 + operand2)
            elif givenExpression[i] == '-':
                tempStack.append(operand1 - operand2)
            elif givenExpression[i] == '*':
                tempStack.append(operand1 * operand2)
            elif givenExpression[i] == '/':
                tempStack.append(operand1 / operand2)

    finalAnswer = tempStack.pop()
    return finalAnswer


givenExpression = '53+82-*'
print('Given postfix expression was',givenExpression,'and it evaluates to ',end='')
print(postfixEvaluation(givenExpression))