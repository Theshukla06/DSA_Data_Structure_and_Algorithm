def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        
n=int(input("Enter Value n :- "))
for i in range(1,n+1):
    print(fib(i))

