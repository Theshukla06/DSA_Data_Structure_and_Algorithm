from collections import deque

class deque:
    def __init__(self):
        self.item=[]
    def is_empty(self,item):
        return self.item==[]  
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.pop()
    def show_data(self):
        return self.item
q=deque()
q.push("Ankit Shukla")
q.push("Ankit Shukla")
print(q.show_data())
#print(q.pop())

