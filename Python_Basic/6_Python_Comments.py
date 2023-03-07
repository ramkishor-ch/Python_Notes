# Purpose of Comments in Python
# Learning to write comments in Python is also a valuable skill. 
# There are several purposes that comments in Python serve, which make them popular. 

# Some of them are-

# Explaining the code.
# Making the code more readable.
# Preventing execution while testing code.

# Types of Comments in Python :

# 1. Single -Line Comments
# The single-line comments in Python are denoted by the hash symbol “#” and includes no white spaces.
# Example :
# This is a Single-Line comment 
# Print “Scaler Academy!” to console 
print("Scaler Academy!") 

# 2. Multi-Line Comments
# Python does not have multi-line comments, but there are two ways we can achieve this –

# a. You can write “#” at the beginning of every line you wish to comment out. 
# This stimulates multi-line comments in Python.
# Example :
#Welcome
#to
#Scaler
#Academy

# b. For including multi-line comments in Python, we make use of the delimiter ("""). 
# The text to be commented is enclosed within the delimiter. 
# when the comment spans more than a few lines.
# Example: 
"""
If you do not want to type # every time for 
every line, you can make use of 
delimiters!
"""


# 3. Docstring Comments
# Docstring is an in-built feature in Python and is usually associated with documentation in Python. 
# They are added right below the functions, classes or modules, and they describe what they do. 
# In Python, Docstring is made available using the doc attribute.

# Example :
def intro():  
  """ 
This function prints Welcome to Scaler
  """  
  print("Welcome to Scaler")              
print(intro.__doc__)