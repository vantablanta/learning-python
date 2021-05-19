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
