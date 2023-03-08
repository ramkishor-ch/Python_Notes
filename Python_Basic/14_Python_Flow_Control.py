# We’re just making decisions and telling how the code should execute in certain situations, 
# which statement to run before or after, etc. 

# Types of Flow Control in Python :
# a. Conditional
# b. Loops

# a. Conditional
#     1. if
#     2. if else
#     3. if elif else



# if Condition:
# Example :
time = 19
 
if time == 9 :
   print("On time")
 
if time > 9 and time <= 19:
   print("10 minutes late") # Output : 10 minutes late
 
if time > 19 and time <= 39:
  print("30 minutes late")
 
if time > 39:
  print("Zero marks")




# if else Condition
# Example :
time = 21
 
if time == 9 :
   print("On time")
else:
    if time > 9 and time <= 19:
        print("10 minutes late")
    else:
        if time > 19 and time <= 39:
            print("30 minutes late")
        else:   
            if time > 39:
                print("Zero marks")




# if elif else Condition
# Example :
time = 40
 
if time == 9 :
   print("On time")
 
elif time > 9 and time <= 19:
   print("10 minutes late")
 
elif time > 19 and time <= 39:
  print("30 minutes late")
 
else:
  print("Zero marks")




# Nested if
# Below is the Python Program to understand the concept around the implementation of nested if statement

# print statement 
print("Case to show how nested if statement in python works.")

# declaring a variable with its value as 50.
number1 = 50

# nested if statement
if number1 > 20:
    print("Nested if condition 1 is satisfied.")
    if number1 > 25:
        print("Nested if condition 2 is satisfied.")
        print(number1, "is a greater than 20 and 25. The `nested if statement` is satisfied." )
print("I am getting printed as I didn't follow the indentation!")

# decalring a variable with its value as 15.
number1 = 15

# nested if statement
if number1 > 20:
    print("Nested if condition 1 is satisfied.")
    if number1 > 25:
        print("Nested if condition 2 is satisfied.")
        print(number1, "is a greater than 20 and 25. The `nested if statement` is satisfied." )
print("I am getting printed as I didn't follow the indentation!")




# If-elif-else Ladder
# Below is the Python Program to understand the concept around the implementation of the Elif statement
 
# print statement 
print("Case to show how elif statement in python works.")

# declaring a variable with its value as 21.
number1 = 21

# elif statement
if number1 > 20:
    print("if condition 1 is satisfied.")
elif number1 > 25:
        print("elif condition 2 is satisfied.")
else:
    print("else condition is satisfied" )
print("I am getting printed as I didn't follow the indentation!")

# declaring a variable with its value as 28.
number1 = 28

# elif statement
if number1 < 20:
    print("if condition 1 is satisfied.")
elif number1 > 25:
        print("elif condition 2 is satisfied.")
else:
    print("else condition is satisfied" )
print("I am getting printed as I didn't follow the indentation!")

# declaring a variable with its value as 28.
number1 = 30

# elif statement
if number1 < 20:
    print("if condition 1 is satisfied.")
elif number1 < 25:
        print("elif condition 2 is satisfied.")
else:
    print("else condition is satisfied" )
print("I am getting printed as I didn't follow the indentation!")




# Short Hand If
# Below is the Python Program to understand the concept around the implementation of shorthand If statement
# print statement  
print("Case to show how shorthand if statement in python works.")

# declaring a variable with its value as 21.
number1 = 21

# short hand If  statement
if number1 > 20:     print(number1 , "is greater than 20")
print("I am getting printed as I didn't follow the indentation!")

# declaring a variable with its value as 8.
number1 = 8

# short hand If statement
if number1 > 50:     print(number1 , "is greater than 50")
print("I am getting printed as I didn't follow the indentation!")



# Short Hand If-Else
# Below is the Python Program to understand the concept around the implementation of shorthand If else statement
 
# print statement 
print("Case to show how shorthand if else statement in python works.")

# declaring a variable with its value as 21.
number1 = 21

# short hand If  else  statement
print(number1 , "is greater than 20") if number1 > 20 else print(number1 , "is lesser than 20")
print("I am getting printed as I didn't follow the indentation!")

# declaring a variable with its value as 8.
number1 = 8

# short hand If  else statement
print(number1 , "is greater than 50") if number1 > 20 else print(number1 , "is lesser than 50")
print("I am getting printed as I didn't follow the indentation!")




# Switch Case Statement in Python

# The advantage of implementing the Switch case statement in python is that it can be considered as an alternative to if-else or if elif else statements,

# Below is the Python Program to understand the concept around the implementation of the Switch case statement in python 
 
# print statement
print("Case to show how Switch case statement in python works.")
 
# defining the SwitchEx function with three cases.
# default return is kept as Nothing.
def SwitchEx(expression):
    switch = {
        0: "Case Zero is encountered",
        1: "Case One is encountered",
        2: "Case Two is encountered",
        }
    return switch.get(expression, "Not a part of Switch Cases")

if __name__ == "__main__":
    expression = 2
    print (SwitchEx(expression))
print("I am getting printed as I didn't follow the indentation!")

if __name__ == "__main__":
    expression = 33
    print (SwitchEx(expression))
print("I am getting printed as I didn't follow the indentation!")

if __name__ == "__main__":
    expression = 1
    print (SwitchEx(expression))
print("I am getting printed as I didn't follow the indentation!")





# Loops :
# a. For Loop
# b. While Loop

# For Loop
students_arrival_time = [9,25,39,45,9,75,84,2,18,13]
 
for student_counter in range(len(students_arrival_time)):
 
    if students_arrival_time[student_counter] == 9 :
        print("On time")
        
    elif students_arrival_time[student_counter] > 9 and students_arrival_time[student_counter] <= 19:
        print("10 minutes late")
       
    elif students_arrival_time[student_counter] > 19 and students_arrival_time[student_counter] <= 39:
        print("30 minutes late")
        
    else:
        print("Zero marks")


# For Else :
# example:
# list of numbers
my_list = [1,2,0,5,3]

for denominator in my_list:
   try:
       30/denominator
   except ZeroDivisionError:
       print("zero division error!")
       break
else:
   print("No zero division error found!")
# Output:
# zero division error!



# The range() function
# range() is a built-in function provided by Python. 
# This function is commonly used with a for loop for looping over a range of numbers. 
# This function returns a sequence of numbers that, by default, starts with zero, increments by 1, and 
# ends at a specified number passed as an argument. 
# However, it is possible to provide this function as an argument for the starting number, increment step size, and 
# the number at which it needs to stop. There are three ways in which a range() function can be used:

# range(stop): 
# It takes one argument and is the default version of the range() function. 
# It will generate a sequence of numbers starting from 0, incrementing by 1, and ending at the specified number count. 
# For example, range(15) will generate the numbers starting at 0 and ending at 14.

# range(start, stop): 
# This will take as an argument the starting and the ending numbers and will generate the sequence incrementing by 1. 
# For example :
# range(5, 10) will generate a sequence of numbers starting at 5 and ending at 9, by default incremented by 1.

# range(start, increment, stop): 
# This version takes the start value, step value by which the series will increment(positive integer) or 
# decrement(negative integer), and ending values parameters and generates the sequence. 
# For example :
# range(6, 2, 21) will generate all the even numbers between 6 and 21. 
# There will be an increment of 2 in successive values as the step size is 2.


# Example :
#Program to iterate through a list using range()
city = ['London', 'Paris', 'Mumbai', 'Sydney', 'California']
size = len(city)
#iterating over the list using the range() function
for x in range(size):
    print("I Love", city[x])
# Output :
# I Love London
# I Love Paris
# I Love Mumbai
# I Love Sydney
# I Love California



# Looping through a string in Python :
# In Python, we can loop through a string. 
# The string is an iterable object containing the sequence of characters. 
# Although Strings are immutable, we can perform operations using the characters to get the desired result.

# There are many ways of iterating through the string in python using a for a loop.

# Method 1: 
# We can iterate over the string character by character until the string gets exhausted. 
# The for loop in each iteration takes one letter from the string and stores it in the variable character, then prints it.

# Method 2: 
# Another way to iterate over the string is using indexing. 
# Since indexing starts at 0, so we can use the range() function which we have seen above. 
# The range() function will take as an argument the stop value, which serves as the end value for the loop.

# Method 3: 
# One more way to iterate over the string is the enumerate() method. 
# The enumerate() takes the string as an argument and returns a key-value pair. 
# Key being the index number by default and value of the corresponding letter in the string. 
# Key can also be other numbers as a counter the starting of which can be passed as an argument.

# Python program to iterate over a string using a for loop.
string_var = 'view'
# Method 1: Iterating over string
for character in string_var:
    print(character, end=' ') 
print('\n')
# Method 2: Iterating using indexing
for i in range(len(string_var)):
    print(string_var[i], end=' ') 
print('\n')
# Method 3: Iterating using enumerate()
for k, v in enumerate(string_var):
    print(v, end=' ')
# Output:
#  v i e w 
#  v i e w 
#  v i e w 



# Nested Loops in Python :
# Python allows the use of a loop within the loop. 
# This is known as nesting. For every single iteration of the outer loop, the inner loop executes all its iterations. 
# For instance, if the outer loop has n iterations and the inner loop has m iterations, 
# then the total number of iterations will be n x m. That is for each iteration of the outer loop. 
# The inner loop will execute m times.

# Example :
# Python program having nested for loops
names = ['Zeeshan', 'Shubham', 'Vikram']
city = ['Bangalore', 'London', 'Paris']
for i in names:
    for j in city:
        print(f'{i} loves {j}.')
# Output:
# Zeeshan loves Bangalore.
# Zeeshan loves London.
# Zeeshan loves Paris.
# Shubham loves Bangalore.
# Shubham loves London.
# Shubham loves Paris.
# Vikram loves Bangalore.
# Vikram loves London.
# Vikram loves Paris.



# break statement :
# Whenever the specified condition is encountered, we use a break statement that takes us out of the python for a loop. 
# However, the break statement can be used without the condition. 
# But with the for loop it is usually accompanied by condition(s) based on the logic of our program when we want to come out from the loop.

# Example :
# Python program using the break statement
numbers = [5, 9, 7, 13, 8, 1, 11]
for i in numbers:
    # Come out of the loop if an even number is encountered.
    if i%2 == 0:
        print("\nBreaking the Loop. Even Value Encountered.")
        break
    print(i, end=' ')
# Output:
# 5 9 7 13
# Breaking the Loop. Even Value Encountered.



# The pass statement in python
# The indentation block of the for loop in python cannot be left blank. 
# Leaving the body of the for loop blank would result in an error. 
# If for some reason, we are required to leave the for loop body blank, then we use a pass statement. 
# By putting the pass statement, we are just telling the loop to execute normally, and controls come out of the loop after all iterations are completed.

# Example :
# Python program having an empty loop
name = 'Interviewbit'
for alphabet in name:
    pass
print(f'The last letter in the name is {alphabet}')
# Output:
# The last letter in the name is t



# The continue statement in python
# The continue is a loop control statement. Using the continue statement, 
# we can stop the current iteration of the loop based on some condition(s), and control again comes to the beginning of the loop with the next iteration.

# Example :
# Python program with the use of continue statement
country = ['India', 'Japan', 'UAE', 'United Kingdom']
for x in country:
    if x == 'Japan':
        continue
    print(x)
# Output:
# India
# UAE
# United Kingdom






# While Loop
students_arrival_time = [9,25,39,45,9,75,84,2,18,13]
 
student_counter = 0
 
while student_counter < len(students_arrival_time):
 
    if students_arrival_time[student_counter] == 9 :
        print("On time")
        student_counter+=1
 
    elif students_arrival_time[student_counter] > 9 and students_arrival_time[student_counter] <= 19:
        print("10 minutes late")
        student_counter+=1
 
    elif students_arrival_time[student_counter] > 19 and students_arrival_time[student_counter] <= 39:
        print("30 minutes late")
        student_counter+=1
 
    else:
        print("Zero marks")


# While Loop with else
count = 0;
while count < 2:
 print("My name is Vidyut")
 count += 1
else:
 print("String is printed ten times!")
# Output :
# My name is Vidyut
# My name is Vidyut
# String is printed 2 times!

# The else is executed only once after the while loop condition returns false, and the loop breaks.



# Single Statement While Loop in Python
# Example :
count = 0
while count < 10: print("I run Infinitely")
# Output:
# The String “I run Infinitely” getting printed on the console in infinity


# The Infinite While Loop in Python
count = 0
while count != 1:
 name = str(input("What is your name? "))
 print("Hi " + name)
# Output :
# What is your name? R
# What is your name? R
# What is your name? R
# .
# .
# Infinite loop



# Continue Statement:
# Continue statement written inside the body of while loop returns the flow of control back to the expression in the header, 
# skipping the execution of the rest of the statements inside the body.

# Example:
count = 0
while count < 10:
 count += 1;
 if(count == 5): continue
 print("The value of the count is " + str(count))
# Output:
# The value of the count is 1
# The value of the count is 2
# The value of the count is 3
# The value of the count is 4
# The value of the count is 6
# The value of the count is 7
# The value of the count is 8
# The value of the count is 9
# The value of the count is 10



# Break Statement:
# Break statement inside the body of a while loop will stop the repeated execution and bring the control out of the while loop. 
# It is like an abrupt force stop of a while loop. If it is a while..else statement, 
# then the else part is also skipped when a break statement is executed. 
# Control jumps directly to the statement below the while..else statements.

# Example:
count = 0
while count < 10:
 count += 1;
 if(count == 5): break
 print("The value of the count is " + str(count))
# Output:
# The value of the count is 1
# The value of the count is 2
# The value of the count is 3
# The value of the count is 4



# Pass Statement:
# A pass statement can be seen as a dummy/empty statement. 
# It is used to write empty loops, empty blocks, empty functions, classes, etc. 
# It doesn’t really affect the flow of control. 
# It is used to keep the flow seamless.

# Example:
count = 0
while count < 10:
 count += 1;
 if(count == 5): pass
 print("The value of the count is " + str(count))
# Output:
# The value of the count is 1
# The value of the count is 2
# The value of the count is 3
# The value of the count is 4
# The value of the count is 5
# The value of the count is 6
# The value of the count is 7
# The value of the count is 8
# The value of the count is 9
# The value of the count is 10