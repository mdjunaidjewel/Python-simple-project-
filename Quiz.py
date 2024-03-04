#-------Quiz-project-Python-------

Question1 = ''' What is correct syntax in Python?

1) echo("Hello World!")
2) p("Hello World!")
3) print("Hello World!")
4) echo "Hello World!"

'''
Question2 = '''Which one is NOT a legal variable name?

1) my_var
2) my-var
3) _myvar
4) Myvar

'''

Question3 ='''What is the correct file extension for Python files?

1) .pyth
2) .pt
3) .py
4) .pyt

'''
Question4 =''' Which method can be used to return a string in upper case letters?

1) upper()
2) toUpperCase()
3) uppercase()
4) upperCase()

'''

Question5 = ''' Which operator is used to multiply numbers?

1) X
2) *
3) #
d) %

'''
#Create Dictionary

Questions = { Question1: "3",
                         Question2:"1",
                         Question3:"3",
                         Question4:"1",
                         Question5:"2",
}

name = input("Enter your Full name: ")
print("Assalamualaikum:",name, "Welcome to the Quiz")


score = 0
for x in Questions:
    print(x)
    answers = input("Enter the correct answer: (1/2/3/4): ")
    
    if answers == Questions[x]:
        print("You are selected the correct answer, You are got 1 point! ")
        score =+1
    else:
        print("<Its the wrong answer, You are lost 1 point>")
        score =-1
        
   
#The-End
