import queue

q=queue.Queue(maxsize=4)
q.put(1)
q.put(2)
q.put(3)
q.put(4)

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print("Full :-",q.full())
print("Empty :-",q.empty())