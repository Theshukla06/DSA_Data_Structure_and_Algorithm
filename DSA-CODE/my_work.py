n=int(input('enter :-'))
if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print('not prime')
            break
        else:
            print('prime')


# a=(1,2,3,4,5)
# print("Array Reverse :- ",a[::-1])


# def Name(name):
#     print(name,'Hy You Are Selected For IT Company Thank You')
# def Age(age):
#     print('Your Age Is :-',age)

# a=input('Enter Your Name :-')
# b=int(input('Enter Your Age :-'))
# Name(a)
# Age(b)