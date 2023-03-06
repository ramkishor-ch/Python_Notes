# Keywords in python are these unique sets of predefined words reserved to perform a specific function or purpose. 
# These keywords are part of the python syntax. 
# Most of them have a purpose very similar to their actual meaning in English. 
# This makes python easy to understand and code.

# According to version 3.8 in python, there are 35 keywords that it supports.


help("keywords")
# Output : list of keywords
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not



# Python Libraries:
# You can use libraries like kwlist, to get a list of keywords supported by the current version of python you are running the code on.
import keyword
print(len(keyword.kwlist))
# Output : 35



# iskeyword() function:
# This function is part of the keyword package and is used to check if a term is a python keyword or not
import keyword
print(keyword.iskeyword("finally"))
print(keyword.iskeyword("hi"))
# Output : 
# True
# False



# Types of Keywords
# 1. Value Keywords
#     These python keywords are used to denote values. 
#     These values are single values that can be used multiple times and about the same object or variable. 
#     These keywords are the only keywords that begin with a capital letter. 

# Keyword	Usage
# True	    Used for assigning the value to a variable or represents the result of a boolean expression evaluating to true
# False	    Used for assigning the value to a variable or represents the result of a boolean expression evaluating to false
# None	    Represents null, nil, none, undef, or undefined values in python

# Example :
print(1 == 1)         # Output : True
print(True or False)  # Output : True
print(3 > 7)          # Output : False
print(True and False) # Output : False
print(None == 0)      # Output : False

x = None
y = None
print(x == y)         # Output : True



# 2. Operator Keywords
# python uses keywords for defining these operators. 
# Their function is similar to their literal meaning, making coding in python lucid to understand. 

# Keyword	Math Operator
# and	    AND, Intersection(^)
# or	    OR, Union(v)
# not	    NOT, Negation (¬)
# in	    CONTAINS, (∈)
# is	    Checking Identity

# Example:
print(True and False) # Output : False
print(True or False)  # Output : True
print(not False)      # Output : True

a = 'scaler academy'
print('scaler' in a) # Output : True
print(True is True)  # Output : True



# 3. Control Flow Keywords
# These keywords help us perform conditional logic and execute code given certain conditions. 
# They are commonly used in forming a pipeline on how the code should perform based on decision-making conditions and 
# hence are essential in python. 

# Keyword	Syntax	                            Function
# if	    if <expression>: <body of code>	    Executes the body of code if the expression evaluates to True
# elif	elif <expression>:<body of code>	Similar to ‘if’, ‘elif’ is used to execute the body of code if the expression evaluates to True. 
#                                             You can use ‘elif’ only after ‘if’ and multiple times. 
#                                             The function literally translates to ‘ else – if ‘.
# else	else:<body of code>	                Executes the body of code when all of the above expressions gets evaluated to False

# Example: # My Calculator
a = int( input() )  # Input : 3
b = int(input())    # Input : 5
print ('enter operation: +, -, *, /')
opt = input()       # Input : +
 
if opt == '+':
    print (a+b)     # Output : 8
elif opt == '-':
    print (a-b)
elif opt == '*':
    print (a*b)
elif opt == '/':
    print (a/b)
else:
    print ('invalid input')



# 4. Iteration Keywords :
# In python programming, these keywords indicate the type of looping initiated. 

# Keyword	 Syntax	                                            Function
# for	     for <element> in <condition>:<body of code>	    Loops the element according to the condition and executes the body of code 
#                                                               until the element is unable to fit in the condition.
# while	     while <condition>:<body of code>	                Executes body of code until condition is evaluated to False
# break	     for <element> in <condition1> <condition2>:break	It exits from the loop if condition2 evaluates to True . 
#                                                               #Also works with while loop
# continue   for <element> in <condition1> <condition2>:continue Continues the looping if condition2 evaluates to True. 
#                                                                Also works with while loop

# Example: # Display numbers 5 to 10
 
# for loop example
for x in range (5,11):
    print (x) 
# Output :
#     5
#     6
#     7
#     8
#     9
#     10

#################################
 
n = 5
# while loop example
while n < 11:          
    print(n)
    n+=1
# Output:
#     5
#     6
#     7
#     8
#     9
#     10



# 5. Structural Keywords
# We use various keywords in python to define the structure of certain pieces of code. 
# These keywords are very often used to make code modular and understandable.

# Keyword	Syntax	                                                Function
# def	    def <name of function>(<parameters>):<body of code>	    Defines the beginning of a function in python
# class	    class <name of class>(<extends>):<body of code>	        Defines the beginning of a class in python
# with	    with <context manager> as <variable>: <body of code>	We use with to run codes within the context manager functions. Like: reading and writing of files
# as	    import <module> as <alias>	                            It is used to provide an alias to modules, functions, etc.
# pass	    def function()	                                        Used with functions classes, if-else statements, etc. to indicate ‘no – operation’ taking place
# lambda	lambda <arguments>:<function>	                        It is used to create a nameless function. It is an inline function that does not contain a return statement.



# 6. Return Keywords
# These keywords help us give out results of functions. 
# They are essential keywords that help us determine with what value must exist the function. 

# Keyword	Syntax	                        Function
# return	def <function>() <statement>	Returns the statement when this function is called
# yield	    def <function>():               Through yield we can have numerous return statements which will perform sequentially using the in built next() function in python
#               … yield <statementl> 
#                … yield <statement2>
#           test = <function() 
#           next(test)<statement1> 
#           next(test)<statement2>	



# 7. Import Keywords :
# There are many useful packages and libraries in python that can be installed and 
# used to form your code that is not available in the installed version of python. 

# Keyword	Syntax	                         Function
# import	import <module>	                 Imports all functions of the specified modules to be used in the python file’s execution.
# from	    from <module> import <function>	 The from keyword is used together with import to import specific functions from a module.
# as	    import <module> as <alias>	     Import module with a alias



# 8. Exception Handling Keywords
# The following keywords are used to raise and catch exceptions in python.

# Keyword	Syntax	                                Function
# try	    try: <statements>	                    Initiates try block where the statement is executed if there is no exception
# except	try:<statement1>
#           except <exception>: <statement2>	    Specifies the type of exception that should occur and what subsequent statements should execute
# raise	    raise <exception>	                    This statement can be used to raise a particular exception to any block of code
# finally	try: <statements>finally:<statements>	Finally defines a piece of code that should run no matter what
# assert	assert <expression>	                    An assert statement will result in performing no operation if the expression is executed as truthful,
#                                                   and it will raise an AssertionError if the expression is executed as False.



# 9. Asynchronous Programming Keywords :
# In python, to perform asynchronous programming, 
# we used keywords defining these functions: async and await.

# Keyword	Syntax	                                    Function
# async	async def <function>(<params>):<statements>	    Indicates that the following function needs to run asynchronously
# await	await <some async function call> 
#                     OR 
#         <var> = await <some async function call>	    It is used in asynchronous functions to specify a point in the function 
#                                                       where control is given back to the event loop for other functions to run



# 10. Variable Handling Keywords
# These keywords are used to do manipulations on python variables.

# Keyword	    Syntax	             Function
# del	        del <variable>	     The keyword is used to reset the variable to an unused one
# global	    global <variable>	 The keyword specifies that the variable is pulled from global scope
# nonlocal	    nonlocal <variable>	 Similar to global, this keyword specifies that the variable has been pulled from parent scope






# What are Python Identifiers?
# An identifier is a name given to entities like variables, class, functions, etc. 
# It helps to differentiate one entity from another and understand the flow of entities in code.

# Example :
#     AbCd
#     aBcDa
#     abc123
#     ABC123
#     abc_123
#     ABC_123