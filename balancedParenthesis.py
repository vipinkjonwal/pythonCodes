def balancedParenthesis(givenString):

    tempStack = []
    top = len(tempStack)-1

    for i in range(len(givenString)):
        if givenString[i] == '(' or givenString[i] == '{' or givenString[i] == '[':
            tempStack.append(givenString[i])
        elif givenString[i] == ')' or givenString[i] == '}' or givenString[i] == ']':
            if givenString[i] == ')' and tempStack[top] == '(':
                tempStack.pop()

            elif givenString[i] == '}' and tempStack[top] == '{':
                tempStack.pop()

            elif givenString[i] == ']' and tempStack[top] == '[':
                tempStack.pop()
            else:
                break
        else:
            continue

    return True if len(tempStack) == 0 else False


givenString = '[]({{()[]}})()'
print(balancedParenthesis(givenString))