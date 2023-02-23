#python is dynamically typed language
#no need to worry for type of an argument or return type of an function

#Section: 1
#function definition
#signature of a function => name of the function with arguments defined
def function_1(name,ID):
    print("printing this function_1")
    print("Name: ",name)
    print("ID: ",ID)

#function calling
function_1("ram",2234)


#Section: 2
#function return
#positional arguments
def addd(x,y):
    return x+y

#the arguments which we are passing are positional arguments
#remember the at which position at which type of argument is passing
addd(3,4)


#Section: 3
#keyword argument
def function_1(name,ID):
    print("printing this function_1")
    print("Name: ",name, "ID: ",ID)

#function calling
function_1(ID=2234, name="ramkishor.ch") #while passing argument order is not a problem


#Section: 4
#default argument of a function
def function_1(name,ID,Department="SOFTWARE"):
    print("printing this function_1")
    print("Name: ",name, ", ID: ", ID,", DEPARTMENT: ",Department)

#function calling
function_1(ID=2234, name="ramkishor.ch")
function_1(ID=23445,name="hari",Department="HARDWARE") #overwrite default arguments


#Section: 5
#By default the access specifier of a function is public


#Section: 6
#private => __functioname():
def __func():
    print("private function")
__func()


#Section: 7
#protect => _functionname()
def _func():
    print("protect function")
_func()


#Section: 8
#python is a dynamically typed, careful when passing parameters in function overloading
def milo(x,y):
    return x+y
def milo(x,y,z):
    return x+y+z
# milo(4,5)
# milo(8,9.6)
# above code error occurs because python is dynamically typed


#Section: 9
#Overcome the above problem, *args is used
# *args => we can pass any number of arguments
def giff(*args):
    tot=0
    for i in args:
        tot+=i
        print(tot)

giff(4)
giff(4,5)
giff(5,6,7)
giff(5,6,7,8)

print("\n")


#Section: 10
# **kwargs => assigning values to variables, passing as keyword argument
# **kwargs => contains the key and value pair
def tall(**kwargs):
    tott=0
    for i in kwargs:
        print("kwargs",i) #default the keys will be printed
    for i in kwargs.values(): #prints only values
        tott+=i
        print("values: ",tott)
    for i in kwargs.keys(): #prints only keys
        print("keys: ",i)
    for i in kwargs.items(): #prints the pair of key and value
        print("key, value",i)
tall(a=1, b=2, c=3, d=5)
tall(a=9)
tall(m=90)

# Output:
# printing this function_1
# Name:  ram
# ID:  2234
# printing this function_1
# Name:  ramkishor.ch ID:  2234
# printing this function_1
# Name:  ramkishor.ch , ID:  2234 , DEPARTMENT:  SOFTWARE
# printing this function_1
# Name:  hari , ID:  23445 , DEPARTMENT:  HARDWARE
# private function
# protect function
# 4
# 4
# 9
# 5
# 11
# 18
# 5
# 11
# 18
# 26


# kwargs a
# kwargs b
# kwargs c
# kwargs d
# values:  1
# values:  3
# kwargs a
# values:  9
# keys:  a
# key, value ('a', 9)
# kwargs m
# values:  90
# keys:  m
# key, value ('m', 90)