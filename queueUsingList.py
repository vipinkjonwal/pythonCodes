def enqueue(queue,item):
    queue.append(item)
    return queue

def dequeue(queue):
    item = queue.pop(0)
    return queue

queue = []
print('Enqueue Operations')
print(enqueue(queue,2))
print(enqueue(queue,3))
print(enqueue(queue,5))
print(enqueue(queue,7))

print('\nDequeue Operations')
dequeue(queue)
print(queue)
dequeue(queue)
print(queue)
