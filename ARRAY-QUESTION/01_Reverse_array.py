# arr=(1,2,3,4,5)
# print("Your Array is :-",arr)
# print("Your Reverse Array is :-",arr[::-1])
# arr = [11, 22, 33, 44, 55]
# print("Before reversal Array is :",arr)
# arr.reverse() #reversing using reverse()
# print("After reversing Array:",arr)

def Reverse(A,start,end):
    while start < end:
        A[start],A[end]=A[end],A[start]
        
        start += 1
        end -= 1
# A=int(input('Enter Number :- '))
A=[1,2,3,4,5,6]
print(A)
Reverse(A,0,5)
print('Your Reverse Array is :- ',A)