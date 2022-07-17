import array 

arr=array.array('i',[1,2,3,4,5])
print("The new created array is : ", end =" ")
for i in range(0,5):
    print(arr[i],end=" ")
print("\r")

arr.append(6)
print('The Append Array is :-',end=" ")
for i in range(0,6):
    print(arr[i],end=" ")
print()

arr.insert(2,8)
print('The Insert Array is :-',end=" ")
for i in range(0,6):
    print(arr[i],end=" ")


# a=array.array('d',[1.1,2.2,3.3,4.4,5.5])
# print("The new created array is : ", end =" ")
# for i in range(0,5):
#     print(a[i],end=" ")
# print()