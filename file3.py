# try and except used when waiting for a promise say in APIs
try : 
    if name :
        print ("The try statment was succesful")
except: 
    print( "the try statemnt failed")

#functions  
def myfunction():
    print("Hello World")
myfunction()

def greeting(name):
    print("Hello"  +" "+name + "!")
greeting("Michelle")

def sum(num1, num2):
    print (num1 + num2)
sum(10, 20 )

def add(a , b):
    return a * b
value = add(5, 30)
print (value)

#inbuilt functions 
#1. abs makes a number positive 
print (abs (-32))
#2. bool returns false for zero and true for any other number 
print (bool(-2))
#3. dir shows allfunctions that can be done to a data type
print (dir("Hey"))
#4. help tells what a function does 
sent= "hello"
help(sent.upper)
#5. eval runs a string as python code 
sen = "print('Hello Michelle')"
eval(sen) #return the string  Hello Michelle
#6. exec does the same as eval but for complicated code like multiline code 