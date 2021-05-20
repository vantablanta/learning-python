#assigning multiple variables the same value 
Sarah = Mike = Bob = 15
print(Bob)

name, age = "Michelle", 25
print (age)

txt = "hi"
print (txt * 10)

# picking certain parts of  a string ..
txt = "Michelle Hi my name is"
print (txt[0:8])#this prints Michelle in the console

#placeholders %s  did not work here but this is an alternative
name = "Uhuru Kenya"
age = 54
sentence = "{} is {} years old and is the president of Kenya".format(name, age )
sentence = f"{name} is {age} years old and is the president of Kenya"
print (sentence)
print (sentence)

#lists.. they are mutable 
shoplist = ['apples', 'oranges', 'bananas', 'mangoes']
print (shoplist)
#accessing items in a list. 
print (shoplist[0]) #returns apples
print(shoplist[0:2]) #splicing a list checks the item from zero to 1 since 2 is not inclusive 
#to add items to the end of the list use the append function. 
shoplist.append('pears')
print(shoplist)
#replacing an element in the strinf with another 
shoplist[0] = 'Cherries'
print(shoplist)
#removing unwanted items from a list method 1
del shoplist[2] #will remove the item at the second index position which is bananas
print(shoplist)
#arithmetic opertaion with lists
#1.finding howmany items are in list 
print(len(shoplist)) #returns 4
#joining lists together 
shoplist2 = ['Bread', "Peanut", 'Jam', 'Bacon']
print (shoplist + shoplist2) #joins the bread list and the cherris list together
#finiding max  and min values
numlist = [1, 10, 50, 2, 6]
print (max(numlist))
print(min(numlist))

#dictionaries data structure basically its an object in js
students = {"Bobo": 12, "Hellen": 15, "Joy": 16}
print(students)
#accessing values students[key]
print (students["Hellen"]) #this will return the age of Hellen 
#updatng values in the dictionaries
students["Hellen"] = 10
print(students)
#removing a key in a dictionary 
del students["Bobo"] 
print (students)
#each Key should be unique,,, dont repeat a key 

#tuples they are imutable sintax below

tup = (1, 2, " Hey")
print (tup)
print (tup[2]) # return hey 
tup2 = (6, 7, "wow")
print (tup + tup2 ) #joins the two tuples together 
print(tup2[1:2]) #tup splicing returns 7 last index is non inclusive

#condiitinal statements. the statement should return a bool 
if (5 > 3):
    print ('Yes it is ')
#adding another outcomeincase the statemnt is not true 
if (3 > 10):
    print ('Yes')
else: 
    print("No you are lying")
    # >= greater than or equal to  <= less than == equal to != no equal to 
    #elif is basically else if 
age = 55
if (age < 13):
    print ("You are a toddler")
elif (age < 21 ):
    print ("You are a teen ")
else:
    print ('You are an adult')

# you can also compare more than two conditions using and & or 

#and returns true if both conditions are true
if( 2 < 5 and 8 > 2):
    print ("Both passed")

#or return true if one of them is true
if( 5< 2 or 8> 2):
    print("One passed")

#for loops aree for iterating thru data structures 
list = ["Cherris", "Bananas", "Apples"]
for item in list: 
    print (item)# prints all the things in the list
tup = (1, 3, 5, 7)
for item in tup :
    print(item)

#iterating thru numbers 
for i in range(0,10):
    print (i) #last index is not included 
#you can specify teh increment factor in the range, to say print out oddd or even numbers

for i in range(0, 11, 2):# prints out the even numbers in a range 
    print(i)

    #first ten multiples of 5
for i in range(0, 51, 5):
    print(i)
    #you can use nested loops but make sure to use diffrent variables 
    #while runs until the condition is false 
     
#control statements are available break , continue and pause



   


