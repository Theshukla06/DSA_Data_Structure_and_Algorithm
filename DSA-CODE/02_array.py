import array

arr=array.array('i',[1,2,3,4,5])
print("The New Array is :- ",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")
print()

print("The Popped Element is :- ",end=" ")
print(arr.pop(2))

print("The After Array Poping is :- ",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")
print()

arr.remove(1)
print("The Array After Removing is :- ",end=" ")
for i in range(0,3):
    print(arr[i],end=" ")

