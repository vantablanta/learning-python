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



