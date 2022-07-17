# from inspect import stack
# from queue import LifoQueue


# stack=LifoQueue(maxsize=3)
# stack.put('Ankit Shukla')
# stack.put('Ankit Shukla')
# stack.put('Ankit Shukla')
# stack.get()
# print(stack.qsize())
# print(stack.full())
# from inspect import stack
# from turtle import st


def Create_stack():
    stack=[]
    return stack

def Empty(stack):
    return len(stack)==0

def Push(stack,item):
   stack.append(item)
   print('Push Iteam In Stack :-'+ item)

def pop(Stack):
    if (Empty(stack)):
        return "Stack Is Empty"
    return stack.pop()

stack=Create_stack()
a=input('Enter Your Name:-')
b=int(input('Enter Your Age :-'))
Push(stack,str(a))
Push(stack,str(b))
















# # from inspect import stack

# # stack=[]
# # a=input('Enter Your Name :-')
# # stack.append(a)
# # b=int(input('Enter Your Age :-'))
# # stack.append(b)
# # print(stack)