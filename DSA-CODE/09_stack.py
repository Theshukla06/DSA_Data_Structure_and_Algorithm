from operator import itemgetter


class Stack:
    def __init__(self):
        self.item=[]
    def is_empty(self,item):
        return self.item==[]
    def Push(self,item):
        return self.item.append(item)
    def pop(self):
        return self.item.pop()

    def Display(self):
        return self.item
    
obj=Stack()
obj.Push("Ankit")
obj.Push("Shukla")

obj.pop()
print(obj.Display())
