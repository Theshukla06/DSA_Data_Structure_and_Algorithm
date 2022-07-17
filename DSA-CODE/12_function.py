def Greeting(language):
    if language == 'English':
       return "Hello I'Am English"
    elif language == 'Hindi':
       return "Hello I'Am Hindi"
    else:
       return "Language Error"
a=input("Enter Your Language :- ")
print(Greeting(a))
