# While performing any operations on variables that have different data types in Python, 
# one of the variable's data types will be changed to the higher data type among the two variables, 
# and then the operation is completed. 

# This automatic conversion of data types done by the interpreter is called implicit type conversion. 
# It does not have any involvement of the user.

# Example :
num1 = 2
num2 = 12.2
res = num1 + num2
print("Data type of num1: ", type(num1))
print("Data type of num2: ", type(num2))
print("Data type of res: ", type(res))
print("Value of res: ", res)
# Output :
    # Data type of num1:  <class 'int'>
    # Data type of num2:  <class 'float'>
    # Data type of res:  <class 'float'>
    # Value of res:  14.2


# But Why is our Result a float?
# The data type conversion is done to prevent the loss of data. 
# Had our result been converted to an int, 
# the fractional portion of the result would have been lost. 

# Hence, the Python compiler converted the smaller data type (int) into a larger one (float) to avoid any data loss.

# Now do you see why conversion to a "higher" data type is necessary and how it prevents loss of data?
# The same way we added two numbers, we can even see the conversion of an int to float when dividing two numbers.

# Example :
num1 = 2
num2 = 5
res = num1/num2
print("Data type of num1: ", type(num1))
print("Data type of num2: ", type(num2))
print("Data type of res: ", type(res))
print("Value of res: ", res)

# Output :
    # Data type of num1:  <class 'int'>
    # Data type of num2:  <class 'int'>
    # Data type of res:  <class 'float'>
    # Value of res:  0.4

# here even though both num1 and num2 were integers, 
# python converted our result to a float to prevent any of the fractional portion of the result to be lost.


# Adding String and Integer:
# Now in the above example, we tried adding int and float, which were both numeric data types and were hence compatible. 
# if we add data types, such as a text data type and a numeric data type.

# Example :
num1 = "2"
num2 = 3
print(num1 + num2)
# Output :
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    # As you can see, we have tried adding a string (higher data type) and an int (lower data type). 
    # One might expect implicit type conversion, but this doesn't happen here as the data types are incompatible.

# The solution to this problem is explicit type conversion.
