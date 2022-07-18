# from numpy import maximum


# a=(1,2,3,4,5)
# print(a)
# print('Max  :-',max(a))
# print(a)
# print('Maximum  :-',min(a))

def maxminposition(A,n):
    mix1= A.index(max(A))
    min2 = A.index(min(A))
    print(max+1)
    print(max-1)

A=list()
n=int(input("Enter size :- "))
print("Enter The Element :- ")
for i in range(int(n)):
    k=int(input(''))
    A.append(k)
maxminposition(A,n)