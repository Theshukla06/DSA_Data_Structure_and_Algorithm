def Pow(a,b):
    
    if b==1:
    
        return a
    
    else:
    
        return a*Pow(a,b-1)

a=int(input("Enter a :- "))
b=int(input("Enter b :- "))

print(Pow(a,b))