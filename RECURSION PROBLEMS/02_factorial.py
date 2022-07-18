def Fact(n):
    if n==1:
        return 1
    else:
        return (n*Fact(n-1))

a=int(input('Enter n :-'))
b=Fact(a)
print(b)