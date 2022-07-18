

def Sum(n):
    if n == 1:
        return 1
    else:
        return (n+sum(n-1))
n1=input('Enter n :-')
a=sum(n1)
print(a)