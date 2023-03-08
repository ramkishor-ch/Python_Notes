# What is Explicit Type Conversion in Python ?
# The conversion of one data type into another, done via user intervention or manually as per the requirement, 
# is known as explicit type conversion. 
# It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), etc.

# Explicit type conversion is also known as Type Casting in Python. 
# So now let’s see the different functions we can use to perform type casting in Python or explicit type Conversion

# Functions :
# int()
# float()
# ord()
# float()
# hex()
# oct()
# tuple()
# set()
# list()
# dict()
# str()

# int() : assigning string to x
# Example :
str = "0010101"
#string type casted to int base 2
base_two = int(str,2)
#default base value 10
base_ten = int(str)
print("Type casted into base 2 :",base_two)
print("Type casted into default base value 10: ",base_ten)
# Output :
# Type casted into base 2 : 21
# Type casted into default base value 10:  10101

# float(x) : assigning string to x
# Example :
sample_str = "0010101"
num = 85
#type casting 
conv_str = float(sample_str)
conv_num = float(num)
print("String converted into floating-point: ",conv_str)
print("Integer converted into floating-point: ",conv_num)
# Output :
# String converted into floating-point:  10101.0
# Integer converted into floating-point: 85.0

# Ord(x) :
# This ord() function converts characters into their integer ASCII value.
# Example :
alphabet = ord('Y')
number = ord('5')
print("Ascii value of character 'Y': ",alphabet)
print("Ascii value of character digit '5': ",number)
# Output :
# Ascii value of character 'Y' : 89
# Ascii value of character digit '5' : 53 

# hex(x): 
# the user can convert an integer into a hexadecimal string.
# Example :
# int to hex
num = 45
conv_num = hex(num)
print("Integer type-casted into hexadecimal string is: ",conv_num)
# Output : 
# 0x2d is equivalent to 45
# Integer type-casted into a hexadecimal string is : 0x2d

# oct(x) :
# this function only converts an integer into an octal string.
# Example :
# int to octal
xval = 45
conv_xvaL = oct(xval)
print("Integer type-casted into octal string is: ",conv_xvaL)
# Output :
# Integer type-casted into octal string is:  0o55 

# tuple(x) :
# function is used to convert data types into a tuple and used to store multiple objects.
# Example :
#string to tuple
input_string = 'Scale'
print(tuple(input_string))
# Output :
# ('S','c','a','l','e')

# set(x) :
# convert any iterable into sets.
# Example :
#string to set
x = 'success'
print(set(x))
# Output :
# {'s', 'e', 'u', 'c'}

# list(string_val) :
# convert an iterable into a list
# Example :
x = 'Scale'
print(list(x))
# Output :
# ['S','c','a','l','e']

# dict(x) :
# convert data type into a dictionary
# Example :
x = (('a',3),('f',4),('t',9))
print(dict(x))
# Output :
# {'a' : 3, 'f': 4, 't': 9}

# str(x) :
# convert any data type into the string data type
# Example :
a = 121
b = 42.0
print(type(a))
print(type(a))
print("Integer into String: ",str(a))
print("Floating point into String: ",str(b))
type(str(a))
print(type(str(a)))
# Output :
# <class 'int'>
# <class 'int'>
# Integer into String: 121
# Floating-point into String: 42.0
# <class 'str'>


