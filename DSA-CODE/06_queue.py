from collections import deque


q=deque()
q.append('Ankit')
q.append('Atul')
q.append('Baba')
q.append('Shukla')


print('POP Operation :-',q.popleft())
print('POP Operation :-',q.popleft())

# import queue

# queue=['A','B','C']
# print(queue)
# queue.append('E')
# print(queue)  
# print('POP Value is :-',queue.pop())
# print(queue)