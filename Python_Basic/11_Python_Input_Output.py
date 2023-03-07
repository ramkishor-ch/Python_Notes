# Python Input :
# take input from the users, in which the users themselves will define the values of the variables.

# The input() statement allows us to do such things in Python.

# Example :
# Here we will take an integer as input from the user.
age = int(input("Enter your age: "))
new = age + 1
name = input("Enter your name: ")
print("Hey! " + name + " Next year you will be " + str(new))

# Output:
# Enter your age: 19
# Enter your name: Ayush
# Hey! Ayush Next year you will be 20


# We again need to convert the integer (‘new’ variable) into a string for concatenation during printing the output.

# Example :
# Here we will take two numbers as input from the user.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
mul = num1 * num2
print("The multiplication of num1 & num2 is: %.2f" % mul)

# Output:
# Enter first number: 2.5
# Enter second number: 2
# The multiplication of num1 & num2 is: 5.00

# In the print() statement we have mentioned “%.2f”. This “.2” specifies that the answer that is to be printed should be up to 2 decimal places.

"""
Python Output :
We use the widely used print() statement to display some data on the screen.

syntax of the print() function. 
This function takes some additional arguments other than objects/values that offer more control over the output format.

Syntax: print(object(s), sep=' ', end='\n', file=file, flush=False)

For your better understanding of the syntax here we have defined a few keywords of the above statement:

object(s) are the values to be printed on the screen. They are converted to strings before getting printed.
sep keyword is used to specify how to separate the objects inside the same print statement. By default, we have it as sep=' ', a space between two objects.
end is used to print a particular thing after all the values are printed. By default, we have end as \n, which provides a new line after each print() statement.
file is used to specify where to display the output. By default, it is sys.stdout (which is the screen).
flush specifies the boolean expression if the output is False or True. By default, it is False. In Python, the output from the print() goes into a buffer. Using the flush= True parameter helps in flushing the buffer as soon as we use the print() statement.

Example : """
print(0, 1, 2)
print(0, 1, 2, sep='$')
print(1, 2, sep='@', end='%')

# Output:
# 0 1 2  # Here we have space between values by default.
# 0$1$2
# 1@2%

# Example :
print("ram", end=' ')
print("rom") # Output: # ram rom
# In the above code snippet, both words were printed in the same line because the end by default wasn’t ‘\n’, instead was ' ' (space)


# Example : We can print a string and number together.
students = 5000
print("ram has " + str(students) + " employees") # Output: # ram has 5000 employees
# While printing numbers and strings together, 
# we need to convert the number into a string to concatenate. 
# The str() is another inbuilt function that converts an integer into a string.


