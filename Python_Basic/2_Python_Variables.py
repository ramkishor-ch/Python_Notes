# Variables : Variables are containers for storing data values.

# Rules :
# The variable name should either begin with an Uppercase(A to Z) or Lowercase(a to z) character or an underscore(_).
# A variable name cannot start with a number
# Always remember to use a MEANINGFUL name for variables in Python. For example – no_of_chocolates makes more sense than noc.
# If a variable has multiple words, it is advised to separate them with an UNDERSCORE.
# A variable name SHOULD NOT be similar to keywords of the programming language.
# Variable names are CASE-SENSITIVE (age, Age and AGE are three different variables).
# A variable SHOULD NOT begin with a digit or contain any white spaces or special characters such as #,@,&.

# Example of good variable names – my_name, my_dob.
# Example of bad variable names – #n, 22dob.




# Multi Words Variable Names :
# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:
# Camel Case : Each word, except the first, starts with a capital letter:
# myVariableName = "John"

# Pascal Case : Each word starts with a capital letter:
# MyVariableName = "John"

# Snake Case : Each word is separated by an underscore character:
# my_variable_name = "John"




# How to Declare a Variable in Python?
# When we assign a value to Python variables, they are automatically declared.
# We use the “=” operator for value assignment.
# Example : 
create_variable = 10



# How to re-declare a Variable in Python?
# We assign a new value to the variable before it is used again.

# Example:
value=111
print("Value as per the first declaration:", value)
value=222
print("Re-declared value:", value)
# Output:
    # Value as per the first declaration: 111
    # Re-declared value: 222



# Assigning a single value to variables in Python
#     Instead of declaring Python variables with the same values one after the other, 
#     Assign a single value to multiple variables.

# Example:
num1=num2=num3=1052
print(num1)
print(num2)
print(num3)
# Output:
# 1052
# 1052
# 1052
 


# Multiple assignments :
# Another ease offered by Python variables is multiple assignments!
# we can declare multiple variables in Python in just one line!

# Example: 
whole_number,str,decimal=10,"Hello World",22.50
print(whole_number)
print(str)
print(decimal)
# Output:
#     10
#     Hello World
#     22.5

# We can easily perform multiple assignments for Python variables just with the , comma operator.



# Variable Types in Python
# Variables have two scopes- global and local. 
# 1. Local Variable in Python
# The variables declared inside a function and used only within the scope of that particular function are known as local variables.

# Example :
def sum():
    num1=10 #local variable
    num2=25 #local variable
    sum=num1+num2
    print(sum)
sum()
# Output : 35

# The local variables num1 and num2 are defined within the function sum and can be referenced only within the scope of sum.

# If we try to refer, say num1, outside the scope –
def sum():
    num1=10 #local variable
    num2=25 #local variable
    sum=num1+num2
    print(sum)
sum()
print(num1) #accessing the variable outside the scope
# Output:
#     We would get the following error –
#     35
#     Traceback (most recent call last):
#     File "main.py", line 7, in <module>
#         print (num1)
#     NameError: name 'num1' is not defined



# 2. Global Variable in Python :
# The variables that can be used throughout the program and its scope are global, 
# available within the entire codebase are known as global variables.
# Any variable declared outside any particular function is considered a global variable.

# Example :
num=30 #global variable
def sum():
    num1=10 #local variable
    num2=25 #local variable
    sum=num1+num2+num #using global variable within a function
    print(sum)
sum()
print(num) #accessing the global variable outside the function
# Output:
#     65
#     30

# we can make out that num has acted as a global variable as we have used it inside and outside the sum() function 
# and we were able to print its value to the console as well.




# How to Delete a Variable in Python?
# Python automatically deletes variables and functions when they can no longer be used, freeing the memory. 
# The user can also manually delete variables and functions. 
# It can be useful when large data structures are no longer needed since deleting them will free memory for other uses. 
# It is why Python offers its users the delete functionality.

# You can delete a variable using the "del" command in Python.

# Example : We declared it initially and now we are deleting it.
no_of_chocolates=10
del no_of_chocolates
print(no_of_chocolates)
# Output :
# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#      print(no_of_chocolates)
# NameError: name 'no_of_chocolates' is not defined

# Using the del command, we have successfully deleted the variable no_of_chocolates.




# Object References :
# Python is an object-oriented language. Hence, every object belongs to a specific class.
# String variables can be declared either by using single or double quotes: x = "John" is the same as x = 'John'
# Example :
message="Welcome to India"  
print(message)
print(type(message))
# Output :
# Welcome to India
# <class 'str'>




# Object Identity : how objects are uniquely identified.
# Python ensures that no two variables will have the same identifier or id. 
# The built-in Python function id() is used to identify the object id or identifier.

# Example that we used to understand object references :
message="Welcome to India"
final_message="Goodbye"
print(id(message))
print(id(final_message))

# we have two different variables- message and final_message. 
# Using the id() function, we are trying to see whether these identifiers are unique or not.

# Output :
# 140706157193616
# 140706157320304



# Casting : If you want to specify the data type of a variable, this can be done with casting.

# Example :
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
# Output :
    # 3
    # 3
    # 3.0



# Output Variables :
# In the print() function, you output multiple variables, separated by a comma:

# Example :
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# Output : Python is awesome

# You can also use the + operator to output multiple variables:
# Example :
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Output : Python is awesome

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# Example :
x = 5
y = "John"
print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas,
# which even support different data types:
# Example :
x = 5
y = "John"
print(x, y)
# Output : 5 John

