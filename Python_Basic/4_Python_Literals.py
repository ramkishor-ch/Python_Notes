# Python literals are quantities/ notations whose value does not change during the execution of a program.

# Literals in Python are nothing but a succinct way of representing the data types. 
# it is the way to represent a fixed value in our source code. 
# They can either be numbers, text, boolean or any other form of data.

# Types of Literals in Python : There are five types of literal in Python
#     String Literals
#     Numeric Literals
#     Boolean Literals
#     Literal Collections
#     Special Literals

# 1. String Literals in Python: 
# Creating a string literal in Python is really easy- enclose the text or the group of characters in single, double or triple quotes. 
# Using triple quotes also allows us to write multi-line strings.

# Single-line String :
# String literals that are enclosed within single quotes (‘’) are known as single-line strings.
# Example :
single_quote = "Welcome"
print(single_quote) # Output: Welcome

# Multi-line String :
# A collection of characters or a string that goes on for multiple lines is a multi-line string.

# These kinds of strings are again implemented in two types-
# a) Adding backslash at the end of every line-
# We can enable multi-line strings in Python by adding a backslash at the end of every line.
# Example: 
str = "Welcome\
to\
Python"
print(str) # Output : Welcome to Python

# b) Using triple quotes :
# Triple quotes at the beginning and end of the string literally will allow us to create a multi-line string in Python easily!
# Example :
str = """Welcome
to 
Python"""
print(str)
# Output :
# Welcome 
# to 
# Python



# 2. Numeric Literals in Python
# Numerical literals in Python are those literals that contain digits only and are immutable.

# 4 Types :

# a. Integer :
# The numerical literals that are zero, positive or negative natural numbers and contain no decimal points are integers.

# The different types of integers are :
# Decimal- It contains digits from 0 to 9. The base for decimal values is 10.
# Binary- It contains only two digits- 0 and 1. The base for binary values is 2 and prefixed with “0b”.
# Octal- It contains the digits from 0 to 7. The base for octal values is 8. In Python, such values are prefixed with “0o”.
# Hexadecimal- It contains digits from 0 to 9 and alphabets from A to F.	

# Example :
x = 1234  #positive whole numbers 
y = -4322 #negative whole numbers
a = 0b10101 #binary literal
b = 505	    #decimal literal
c = 0o350	#octal literal
d = 0x12b	#hexadecimal literal

print(x,y)
print(a,b,c,d)

# Output :
# 1234 -4322
# 21 505 232 299


# b. Float :
# The floating-point literals are also known as real literals. Unlike integers, these contain decimal points.
# Float literals are primarily of two types-
# A. Fractional- Fractional literals contain both whole numbers and decimal points.
# Example:
print(78.256)	# Output: 78.256

# B. Exponential- Exponential literals in Python are represented in the powers of 10. 
# The power of 10 is represented by e or E. 
# An exponential literal has two parts- the mantissa and the exponent.

# Note:
# Mantissa-The digits before the symbol E in an exponential literal is known as the mantissa. 
# In computing, it denotes the significant digits of the floating-point numbers.
# Exponent- The digits after the symbol E in an exponential literal are the exponent. 
# It denotes where the decimal point should be placed.
# Example : 
print(2.537E5) # Output :	253700.0


# c. Complex :
# Complex literals are represented by A+Bj. Over here, A is the real part. 
# And the entire B part, along with j, is the imaginary or complex part. 
# j here represents the square root of -1, which is nothing but the iota or i we use in Mathematics.

# complex literal
a = 7 + 8j
b=5j
print(a)
print(b)

# output : 
(7+8j)
5j


# d. Long :
# Long literals were nothing but integers with unlimited length. 
# From Python 2.2 and onwards, the integers that used to overflow were automatically converted into long ints. 
# Since Python 3.0, the long literal has been dropped. 
# What was the long data type in Python 2 is now the standard int type in Python 3.

# Long literals used to be represented with a suffix- l or L. 
# The usage of L was strongly recommended as l looked a lot like the digit 1.

# Example :
#usage long literal before it was depreciated
# x=037467L 
# print(x)

# Note– The code snippet was executed using Python 1.8. 

# Output :
# Success #stdin
# Success #stdin #stdout 0.01s 7320KB
# 16183



# 3. Boolean Literals in Python :
# Boolean literals in Python are pretty straight-forward and have only two values-

# True- True represents the value 1.
# False-False represents the value 0.

# Example :
#boolean literals
x = (1 == 1)  
y = (7 == False) 
print("x is", x)  
print("y is", y)

# Output :
# x is True
# y is False

# We can see that we used boolean literals for comparison and based on the conditions, 
# we received the outputs True and False, respectively.



# 4. Special Literals in Python
# Python literals have one special literal known as None. 
# This literal in Python is used to signify that a particular field is not created.

# Python will print None as output when we print the variable with no value assigned to it. 
# None is also used for end of lists in Python.

# Example :
#special literals
val=None
print(val) # Output : None



# 5. Literal Collections in Python :
# If we wish to work with more than one value, then we can go for literal collections in Python. 
# Literal collections in Python are of four types-

# a. List Literals :
# Lists are a collection of data declared using the square brackets([]), and 
# commas separate the elements of the list (,). 
# This data can be of different types. 
# Another important thing to know about lists is that they are mutable(changeable).

# Example :
# list literals
numbers = [10, 20, 30, 40, 50]
names = ['John', 'Jake', 'Jason', 25]
print(numbers) # Output : [10, 20, 30, 40, 50]
print(names) # Output : ['John', 'Jake', 'Jason', 25]


# b. Tuple Literals :
# The literals that are declared using round brackets and can hold any data type are tuples. 
# Commas separate the elements of tuples. However, unlike lists, tuples are immutable(unchangeable).

# Example :
# tuple literals
even_numbers = (2, 4, 6, 8)
vowels=('a','e','i','o','u')  
print(even_numbers) # Output : (2, 4, 6, 8)
print(vowels) # Output : ('a', 'e', 'i', 'o', 'u')


# c. Dictionary Literals :
# Dictionary is a collection of data that stores value in a key-value format. 
# These are enclosed in curly brackets and separated by commas. 
# Dictionaries are mutable and can also contain different types of data.

# Example :
# dictionary literals
my_dict = {'a': 'apple', 'b': 'bat', 'c': 'car'}
print(my_dict) # Output : {'a': 'apple', 'b': 'bat', 'c': 'car'}


# d. Set Literals :
# Set literals are a collection of unordered data that cannot be modified. 
# It is enclosed within curly brackets and separated by commas.

# Example : 
#set literals
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels) # Output : {'o', 'e', 'a', 'u', 'i'}

