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

#7. str converts the input to string 
#8. float converts the input to decimal number 
#9. int converts the input to a number 
print (str(458))
print (int(78.55))
print (float(5))

#object oriented programing  consists of classes and objects 
class person:
    def parent(self):
        print ("this is the parent")
p = person() #creating an instance of the person class 
print(p)
print (p.parent())

class person:
    def getName(self):
        print("Michelle")
    def getAge(self):
        print(25)  
p = person()
age = p.getAge()
print(age)

#passing different keys other than self
class person :
    def __init__(self, name, age):
       self.name = name
       self.age = age
    def getName(self):
        print ("My name is "+ self.name)
    def getAge(self):
        print ("I am "+ self.age + " years old")
p = person("Hailey", "16")
print (p.getAge())

#inherintance means basically the child classes inherit from the parent class 
class parent: 
    def __init__(self) :
        print("this is the parent class")
    def parentFunc(self):
        print("this is the parent function")
p = parent()
print (p.parentFunc())
class child(parent):
    def __init__(self):
        print("this is the child class")
    def childFunc(self):
        print("this is the child function ")
c = child()
print (c.childFunc())
#but you can also get the methods(functions stored in 
# the parent since you inheritd them thru the parent class)
print (c.parentFunc())

# WHEN A FUNCTION IN THE CHILD CLASS IS SIMILAR TO 
# ONE IN THE PARENT BUT PRINTING DIFFERENT THINGS TO THE CONSOLE 
# THE CHILD FUNCTION THATS BEEN REINITILAIZED TAKES PRECEDNCE 