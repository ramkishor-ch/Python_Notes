#python is dynamically typed language
#no need to worry for type of an argument or return type of an function

#Types of Functions
# a. Built in Functions
# b. User Defined functions

# a. Built in Functions
# The functions which are already defined in Python.
# Example: 1
x = abs(-7.77)
print("The absolute value is: ", x)     #Output: The absolute value is:  7.77

# Example: 2
# id() is a built-in function in Python that gives memory addresses of objects being passed.
def main():
   i = 5
   print(f"Initial value of i in main: {i}")        #Output: Initial value of i in main: 5
   print(f"Initial address of i in main: {id(i)}")  #Output: Initial address of i in main: 9756352
main()

# b. User Defined Functions
# Section: 1
# function definition
# signature of a function => name of the function with arguments defined
def function_1(name,ID):
    print("printing this function_1")   #Output: printing this function_1
    print("Name: ",name)    #Output: Name: ram
    print("ID: ",ID)    #Output: ID: 2234

# function calling
function_1("ram",2234)


# Section: 2
# function return
# positional arguments
def addd(x,y):
    return x+y

# the arguments which we are passing are positional arguments
# remember the at which position at which type of argument is passing
addd(3,4)


# Section: 3
# keyword argument
def function_1(name,ID):
    print("printing this function_1")   #Output: printing this function_1
    print("Name: ",name, "ID: ",ID)     #Output: ram ID: 2234

# function calling
function_1(ID=2234, name="sriram") #while passing both KEYWORD argument order is not a problem

# function_1(1234, name="hari") # one positional, one keyword argument


# Section: 4
# Default Argument of a function or Required arguments
def function_1(name,ID,Department="SOFTWARE"): 
    print("printing this function_1")                               #Output: printing this function_1
    print("Name: ",name, ", ID: ", ID,", DEPARTMENT: ",Department)  #Output: Name:  ram , ID:  2234 , DEPARTMENT:  SOFTWARE

# default argument ALWAYS should be on right side of the LAST argument in function definition otherwise error occurs
# Example:
# def function_1(Department="SOFTWARE",name,ID):
    #print("Name: ",name, ", ID: ", ID,", DEPARTMENT: ",Department)  #Output: Error occurs

# function calling
function_1(ID=2234, name="ram")
function_1(ID=23445,name="hari",Department="HARDWARE") #overwrite default arguments
# function_1() #Output: error

#Required arguments
"""
def add_nums(num1, num2=12):
    print(num1 + num2)
add_nums(num1=11, num2=13)  # Output: 24
 
# no value for default argument
add_nums(num1=11)  # Output: 23 
 
# no value for required argument
add_nums(num2=13) # Will throw an error 
"""

# Section: 5
# By default the access specifier of a function is public


# Section: 6
# private => __functioname():
def __func():
    print("private function")   #Output: private function
__func()


# Section: 7
# protect => _functionname()
def _func():
    print("protect function")   #Output: protect function
_func()


# Section: 8
# python is a dynamically typed, careful when passing parameters in function overloading
def milo(x,y):
    return x+y
def milo(x,y,z):
    return x+y+z
# milo(4,5)
# milo(8,9.6)
# above code error occurs because python is dynamically typed


# Section: 9
# Overcome the above problem, *args is used
# *args => we can pass any number of arguments or VARIABLE Length Arguments or Arbitrary Arguments
def giff(*args):
    tot=0
    for i in args:
        tot+=i
        print(tot,end=" ")  #Output: 4 4 9 5 11 18 5 11 18 26

giff(4)
giff(4,5)
giff(5,6,7)
giff(5,6,7,8)

print("\n")


# Section: 10
# **kwargs => assigning values to variables, passing as keyword argument
# **kwargs => contains the key and value pair
def tall(**kwargs):
    tott=0
    for i in kwargs:
        print("kwargs",i,end=" ") #default the keys will be printed 
        #Output: kwargs a kwargs b kwargs c kwargs d

    for i in kwargs.values(): #prints only values
        tott+=i
        print("values: ",tott,end=" ")  #Output: values:  1 values:  3 values:  6 values:  11

    for i in kwargs.keys(): #prints only keys
        print("keys: ",i,end=" ")       #Output: keys:  a keys:  b keys:  c keys:  d 

    for i in kwargs.items(): #prints the pair of key and value
        print("key, value",i)   #Output: key, value ('a', 1) key, value ('b', 2) key, value ('c', 3) key, value ('d', 5)

tall(a=1, b=2, c=3, d=5)
tall(a=9)   #Output: kwargs a values:  9 keys:  a key, value ('a', 9)
tall(m=90)  #Output: kwargs m values:  90 keys:  m key, value ('m', 90)

# Section: 11
# How many ways we can pass parameters to function?
# There are two ways
# a. Pass by value or call by value
# b. Pass by Reference or call by reference

# a. Pass by Value:
# copy of the parameter’s value is stored in the memory, and all changes are done to that. 
# Hence, these changes aren’t reflected in the parameter in the function call. 
# Example:
string = "Good Evening."
def greet(string):
   string = "Good Morning"
   print("Inside Function:", string)    #Output: Inside Function: Good Morning
greet(string)
print("Outside Function:", string)      #Output: Outside Function: Good Evening.

# b. Pass by Reference:
# copy of the address of the actual parameter is stored; thus, changes inside the Function will be reflected back in the program.
# Example:
# Python code to demonstrate call by reference
def append_to_list(list1):
   list1.append(35)
   print("Inside Function: ", list1)        #Output: Inside Function:  [5, 10, 15, 20, 25, 30, 35]
multiples_of_5 = [5,10,15,20,25,30]
append_to_list(multiples_of_5)
print("Outside Function: ", multiples_of_5) #Output: Outside Function:  [5, 10, 15, 20, 25, 30, 35]


# Section: 12
# Recursive Functions
#calculate the sum of n consecutive natural numbers recursively
def rec_sum(n):
    if n<=1:
        return n
    else:
        return n + rec_sum(n-1)
y = rec_sum(5)
print(y) #Output: 15

# Section: 13
#An anonymous in python is a function that is defined without a name. 
# Unlike functions defined using the def keyword, these are defined using the lambda keyword and are hence called lambda functions. 
# They can have 0 or more arguments but only one return value.
square = lambda x: x * x
print(square(2)) #Output: 4
