# Booleans represent one of two values: True or False.

# Boolean Values :
print(10 > 9)  # Output : True
print(10 == 9) # Output : False
print(10 < 9)  # Output : False

# Print a message based on whether the condition is True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a") 
else:
  print("b is not greater than a") # Output : b is not greater than a


# Evaluate Values and Variables :
# The bool() function allows you to evaluate any value, and give you True or False in return,

# Example : Evaluate a string and a number:
print(bool("Hello")) # Output : True
print(bool(15))      # Output : True

# Example : Evaluate two variables:
x = "Hello"
y = 15
print(bool(x)) # Output : True
print(bool(y)) # Output : True


# Numbers as a Boolean Value : Most Values are True 
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# Example : The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# Sequences as a Boolean Value : Some Values are False 
# In fact, there are not many values that evaluate to False, except empty values, 
# such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
# Example : The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# One more value, or object in this case, evaluates to False, 
# and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
# Example :
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) # Output : False


# Functions can Return a Boolean : You can create functions that returns a Boolean Value:
# Example : Print the answer of a function:
def myFunction() :
  return True
print(myFunction()) # Output : True



# You can execute code based on the Boolean answer of a function:
# Example :
# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True
if myFunction():
  print("YES!") # Output : YES!
else:
  print("NO!")



# Python also has many built-in functions that return a boolean value, 
# like the isinstance() function, which can be used to determine if an object is of a certain data type:
# Example : Check if an object is an integer or not:
x = 200
print(isinstance(x, int)) # Output : True


""""
1. Comparison operators :
Operator	Title	                    Description	                                                                                    Example	                                Output
==	        Equal to	                It results in a True if the 2 operands are equal, and a False if unequal.	                    print(1==1) print((10-5+2)==(7-9+1))	True False
!=	        Not equal to	            It results in a True if the 2 operands are unequal, and a False if equal.	                    print(3!=2) print((7-1*2)!=(8*2+4))	    True True
<	        Less than	                It results in a True if the first operand is smaller than the second, else a False.	            print(1<1) print((10-5+2)<(7-9+1))	    False False
>	        Greater than	            It results in a True if the first operand is greater than the second, else a False.	            print(1>1) print((10-5+2)>(7-9+1))  	False True
<=	        Less than or equal to	    It results in a True if the first operand is lesser than or equal to the second, else a False.	print(3<=2) print((7-1*2)<=(8*2+4)	    False True
>=	        Greater than or equal to	It results in a True if the first operand is greater than or equal to the second, else a False.	print(1>=1) print((10-5+2)>=(7-9+1))	True False
"""


# 2. Logical Operators
# The logical operators and, or and not are also referred to as Boolean operators. 
# and and or require 2 operands and are thus called binary operators. On the other hand, 
# not is a unary operator which works on one operand.

# and	    True if both are True
# Example :
x = 5
y = 10
z = 11
print((x > y) and (y > z))
print((x > y) and (y < z))
print((x < y) and (y > z))
print((x < y) and (y < z))

# Output:
# False
# False
# False
# True


# or	True if at least one is True
# Example:
x = 5
y = 10
z = 11
print((x > y) or (y > z))
print((x > y) or (y < z))
print((x < y) or (y > z))
print((x < y) or (y < z))

# Output:
# False
# True
# True
# True


# not	True only if False
# Example:
x = True
y = False
print(not x)
print(not y)

# Output:
# False
# True


# Chaining Comparison Operators
# Comparison operators can be chained to summarize the output of 2 or more operations.
# Example:
print(1 < 2 < 3)
print(1 < 2 and 2 < 3)

# Output:
# True
# True


# The types and operations in a chain can be mixed as long as they are comparable.
# Example:
print(1 == 1.0 > 0.75)
print(2 == 2.0 < 1.5)
print(3 < 2 < "2")

# Output:
# True
# False
# False


# Chaining is useful while checking for ranges in real-world models. 
# Example :
grade = 95
print(100 >= grade >= 80) # Output: True



# Short-Circuit Chaining : 
# when the execution of a boolean chain stops when the truth value of an expression has been determined. 
# If chains use an implicit and, it means there will be some kind of short-circuiting caused too.

# Short-circuit chains can also prevent exceptions like ZeroDivisionError.

# Example :
print(3 < 2 < (1//0)) # Output: False



