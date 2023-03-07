# Strings :
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# Example : 'hello' is the same as "hello".

# Assign String to a Variable :
# Example :
a = "Hello"
print(a) # Output : Hello

# Multiline Strings : You can assign a multiline string to a variable by using three quotes
# Example :
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Output :
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

# Get the character at position 1 (remember that the first character has the position 0):
# Example :
a = "Hello, World!"
print(a[1]) # Output : e

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Example :
for x in "banana":
  print(x)
# Output :
# b
# a
# n
# a
# n
# a

# String Length
# To get the length of a string, use the len() function.
# Example :
a = "Hello, World!"
print(len(a)) # Output: 13

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword "in".
# Example :
txt = "The best things in life are free!"
print("free" in txt) # Output : True

# Print only if "free" is present:
# Example :
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") # Output : Yes, 'free' is present.

# Check if NOT :
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Example :
txt = "The best things in life are free!"
print("expensive" not in txt) # Output : True

# print only if "expensive" is NOT present:
# Example :
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") # Output : No, 'expensive' is NOT present.




# Slicing :
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Example : Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5]) # Output : llo


# Slice From the Start : By leaving out the start index, the range will start at the first character:
# Example : Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5]) # Hello


# Slice To the End : By leaving out the end index, the range will go to the end:
# Example : Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:]) # Output : llo, World!


# Negative Indexing : Use negative indexes to start the slice from the end of the string:
# Example : Get the characters
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2]) # Output : orl




# Modify Strings :

# Upper Case :
# Example : 
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper()) # Output : HELLO, WORLD!

# Lower Case :
# Example : 
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower()) # Output : hello, world!

# Remove Whitespace :
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# Example : 
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String :
# Example : 
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J")) # Output : Jello, World!

# Split String :
# The split() method returns a list where the text between the specified separator becomes the list items.
# Example : 
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']




# String Concatenation : 

# To concatenate, or combine, two strings you can use the + operator.
# Example : 
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c) # Output : HelloWorld

# Example : 
# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c) # Output : Hello World




# Python Output Formatting - Strings :

# We can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

# Example : Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) # Output : My name is John, and I am 36

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# Example :
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) # Output : I want 3 pieces of item 567 for 49.95 dollars.

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# Example :
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # Output : I want to pay 49.95 dollars for 3 pieces of item 567.




# Escape Character :

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

# The escape character allows you to use double quotes when you normally would not be allowed

# Example :
txt = "We are the so-called \"Vikings\" from the north."

txt = 'It\'s alright.'
print(txt) # Output : It's alright.

txt = "This will insert one \\ (backslash)."
print(txt) # Output : This will insert one \ (backslash).

txt = "Hello\nWorld!"
print(txt) 
# Output : 
# Hello
# World

txt = "Hello\rWorld!"
print(txt) # Output : World!

txt = "Hello\tWorld!"
print(txt) # Output : Hello   World!

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) # Output : HelloWorld!

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) # Output : Hello

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) # Output : Hello


