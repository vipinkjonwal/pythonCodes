def balancedParenthesis(givenString):

    tempStack = []
    top = len(tempStack)-1

    for i in range(len(givenString)):
        if givenString[i] == '(' or givenString[i] == '{' or givenString[i] == '[':
            tempStack.append(givenString[i])
            print(givenString[i],tempStack)
        else:
            if givenString[i] == ')' and tempStack[top] == '(':
                tempStack.pop()
                print(givenString[i],tempStack)

            elif givenString[i] == '}' and tempStack[top] == '{':
                tempStack.pop()
                print(givenString[i],tempStack)

            elif givenString[i] == ']' and tempStack[top] == '[':
                tempStack.pop()
                print(givenString[i],tempStack)
            else:
                break

    return True if len(tempStack) == 0 else False


givenString = '[]({{()[]}})()'
print(balancedParenthesis(givenString))