# Python Indentation Rules:
    # Python uses four spaces as default indentation spaces. A minimum of one space is needed to indent a statement.
    # The first line of python code cannot have an indentation.
    # Indentation is mandatory in python to define the blocks of statements.
    # The number of spaces must be uniform in a block of code.
    # It is preferred to use whitespaces instead of tabs to indent in python. Also, either use whitespace or tabs to indent; 
        # intermixing of tabs and whitespaces in indentation can cause wrong indentation errors.


# Examples :
# Wrong Indentation(Error):
# if( 1 == 1):
# print("This is test code")

# With Correct Indentation:
if( 1 == 1):
  print("This is test code")



# Wrong Indentation(Error):
# if( 1 == 1):
#  print("This is test code")
#     print("This is test code1")

# With Correct Indentation:
if( 1 == 1):
 print("This is test code")
 print("This is test code1")



# Wrong Indentation(Error):
# if( 1 == 1):
# print("This is test code")
# print("This is test code1")

# With Correct Indentation:
if( 1 == 1):
 print("This is test code")
 print("This is test code1")



# Wrong Indentation(Error):
# if( 1 == 1):
#    print("This is test code")
 
#  print("This is test code1")

# Correct Indentation:
if( 1 == 1):
   print("This is test code")
 
   print("This is test code1")


