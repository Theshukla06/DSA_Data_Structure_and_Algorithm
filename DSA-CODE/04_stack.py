from inspect import stack
from turtle import st

stack = []
print(stack)
#APPEND VALUE IN STACK
stack.append('Bhumi')
stack.append('Ankit')
stack.append('Shukla')
stack.append('Aman')
stack.append('Anmol')
print("Your Stack Value is :-",stack,end=" ")
print()
#USING POP ELEMENT IN STACK

print('Element pop from stack :- ',(stack.pop()))
print('Element pop from stack :- ',(stack.pop()))
print('Element pop from stack :- ',(stack.pop()))

print("After pop stack :-",stack)

