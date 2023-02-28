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


# example of a function that uses standard arguments, *args and **kwargs in Python:
def printingData(codeName, *args, **kwargs):
    print("I am ", codeName)            #Output:   I am 007 
    for arg in args:
        print("I am arg: ", arg)        #Output: I am arg: agent 
    for keyWord in kwargs.items():
        print("I am kwarg: ", keyWord)  #Output:   I am kwarg: (‘firstName’, ‘James’) 
                                                  #I am kwarg: (‘lastname’ , ‘Bond’)
 
printingData('007', 'agent', firstName='James', lastName='Bond') 



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
# Recursive Functions: Function calling itself until the base condition is satisfied
# calculate the sum of n consecutive natural numbers recursively
def rec_sum(n):
    if n<=1:
        return n
    else:
        return n + rec_sum(n-1)
y = rec_sum(5)
print(y) #Output: 15

# Types of Recursion in Python
# There are mainly 2 types of recursive functions:
# 1) Direct Recursion : In this type of recursion, the function calls itself.
    # a) Tail Recursion : A recursive call is said to be tail-recursive if it is the last statement to be executed inside the function.
    # b) Head Recursion : A recursive function, the last statement is not a recursive call, during the unwinding phase, 
                         # there are still some steps to occur, and then it is called head recursion.
# 2) Indirect Recursion : In this type of recursion, the function calls another function which calls the original function. 
# Here, when function A() is called, it first executes the print statement and then calls function B() with an incremented value of n. 
# Its print statement is executed within function B, and then the function A() with a value of n reduced by five is called.
# The process continues as long as the terminating condition is not satisfied.

# Example : Tail Recursion
def dispn(n):
    if n == 0:
        return  # Base case
    print(n)
    dispn(n - 1)  # Tail Recursive Call
dispn(5)

""" 
Output:
5
4
3
2
1
"""

# Example : Not Tail-Recursive:
def dispn(n):
    if n == 0:
        return  # Base case
    dispn(n - 1)  # Not a Tail Recursive Call
    print(n)
dispn(5)

"""
Output:
1
2
3
4
5
"""

# Example : Head Recursion
def headr(n):
    if n > 0:
        headr(n - 1)
        print(n, end=" ")
p = 5
headr(5)

"""
Output:
1 2 3 4 5
"""

# Example : Indirect Recursion
def A(n):
    if n > 0:
        print("", n, end='')
        B(n + 1)

def B(n):
    if n > 1:
        print("", n, end='')
        A(n - 5)

A(20)
"""
Output:
 20 21 16 17 12 13 8 9 4 5
"""


# Section: 13
# An anonymous in python is a function that is defined without a name. 
# Unlike functions defined using the def keyword, these are defined using the lambda keyword and are hence called lambda functions. 
# They can have 0 or more arguments but only one return value.

#  lambda function, we can pass multiple arguments but only a single expression

# Syntax:
# lambda [arguments] : expression
square = lambda x: x * x
print(square(2)) #Output: 4


# built in functions: filter(), map(), reduce()


# a. Lambda Function Inside the filter() Function
# When we call the filter function, it iterates over the provided list and passes every value one by one to the function, 
# which returns true or false.
# If that particular value's result is true, it gets added to the list. 

#List of numbers
numbers = [1,2,3,4,5,6,7,8]

# Syntax: filter(function, list)
# one liner code to make list of even numbers using filter() function
even_no = list(filter((lambda x : x % 2 == 0), numbers))
 
# even numbers list
print(even_no) #Output: [2, 4, 6, 8]


# b. Lambda Function Inside the map() Function
# The Python map() function is mostly used to modify the items in the list.
# The map() function iterates over the list provided as a parameter and each value is passed as a parameter to evaluate with the expression of the lambda function. Then these evaluated values get returned one after another.

# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# One liner code to create the list of squares of the numbers using map() function
# Syntax : map( function, list)
sq_numbers = list(map((lambda x : x*x), numbers))
 
# Printing the new list
print(sq_numbers) #Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# c. Lambda Function Inside reduce() Function
# The Python reduce() function is mostly used to reduce the entire list into a single result.
# The reduce() function needs to be imported from the functools module. Functools is one of the modules in python which contains some higher-order functions.
# The reduce() function iterates over the given list of numbers, and these numbers are passed to the lambda function as a parameter. 
    # When the entire list is iterated, the final result is returned by the reduce() function.

#importing reduce() function from functools module
from functools import reduce
 
# Given list of numbers
numbers = [ 1, 2, 3, 4, 5, 6]

# Syntax : reduce( function, list)
# One liner code to do the addition of all numbers using reduce() function
sum = reduce((lambda x, y: x + y), numbers)
 
# Result of addition
print(sum) #Output: 21




# Section: 14
# Packing and UnPacking Arguments
# *args and **kwargs. *args stands for positional arguments and **kwargs stands for keyword arguments.
# Both \* and \*\* are the operators that perform packing and unpacking in Python. 
# \* operator (associated with args) with any iterable (tuple, list, and strings), 
# \*\* operator (associated with kwargs) can only be used on dictionaries.

# Packing Arguments:
# It is simply ‘packing’ the arguments into a single variable (i.e., a tuple of all arguments) that a function call will receive.
# It means that the elements inside a function can individually be accessed in the same way as for tuple values, 
# i.e., tuple[0], tuple[1] etc. Furthermore, it also helps us convert the tuple into a list that can be manipulated.

# Example to Understand PACKING with * Operator
# A Python program to demonstrate packing
# All arguments passed to fun2 are packed into tuple *args.
def fun2(*args):
    # Accessing the elements just like we access then from a tuple
    print(args[0])
 
    # Convert args tuple to a list so we can modify it
    args = list(args)
 
    # Modifying args
    args[0] = 'Scaler'
    args[1] = 'Academy'
    print(args)     #Output: Python
                            #['Scaler', 'Academy', 'preparation']
fun2('Python', 'programming', 'preparation')

# Unpacking Arguments:
# tuple with any number of values. In such times, unpacking is used.
# Supposing 1, 2, 3, 4, 5 are going to be function parameters
# We want to add these numbers

values = (1, 2, 3, 4, 5)
 
def add_numbers(*args):
  total = 0
  for num in args:
    total += num
  print(total)      # Output: 15
  return total
 
add_numbers(*values)



# PACKING Arguments: ** operator
# we can use ** to perform packing of keyword arguments that are passed to a function. 
# how an input (in the form of key:value pairs) to our function can be packed into a dictionary.
# A Python program to demonstrate packing of dictionary items using **
def fun(**kwargs):
    # Printing dictionary items
    print(kwargs)   #Output: {'name': 'Scaler Academy', 'ID': '001', 'language': 'Python'}
fun(name="Scaler Academy", ID="001", language="Python") #all the arguments we passed as input to our function are now inside a dictionary.

# We can easily access these dictionary items by:
# Packing of dictionary items using **
def fun(**kwargs):
    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))   # Output:
                                                # name = Scaler Academy
                                                # ID = 001
                                                # language = Python
fun(name="Scaler Academy", ID="001", language="Python")


# UNPACKING Arguments: ** operator:
# ** operator is used to unpack arguments from dictionaries and perform operations on them seamlessly.
# function that takes three input arguments. The argument names are the same as the keys of the dictionary. 
# This is where the ** operator will be helpful to us. 
# We can easily unpack our dictionary during the function call without having to type out each parameter separately.

def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)    # Output: arg1: InterviewBit
    print("arg2:", arg2)    # Output: arg2: Blog
    print("arg3:", arg3)    # Output: arg3: Packing and Unpacking
     
# Using **kwargs to pass arguments to this function : 
kwargs = {"arg1" : "InterviewBit", "arg2" : "Blog", "arg3" : "Packing and Unpacking"}
myFun(**kwargs)



# PACKING and UNPACKING Arguments: * Operator
# Example:
def print_eligibility(name, age, eligibility):
    print(f'Hey {name}, you are {eligibility} to vote.')  #Output: Hey Anshika, you are not eligible to vote.    
 
def check_eligibility(*args):
    # Convert args tuple to a list so we can modify it
    args = list(args)
    if args[1] >= 18:
        elig = 'eligible'
    else:
        elig = 'not eligible'
    
    args.append(elig)
    print_eligibility(*args)
 
check_eligibility('Anshika', 15)

