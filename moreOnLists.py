def push(stack,item):
    stack.append(item)
    return stack

def myPop(stack):
    item = stack.pop()
    return item

stack = []
print('Pushing onto Stack')
print(push(stack,2))
print(push(stack,3))
print(push(stack,5))
print(push(stack,7))

print('\nPop from Stack')
myPop(stack)
print(stack)
myPop(stack)
print(stack)
