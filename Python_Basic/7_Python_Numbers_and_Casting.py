"""
Python Numbers :
There are 3 numeric types in Python:
a. int
b. float
c. complex
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print((x)) # Output : 1
print((y)) # Output : 2.8
print((z)) # Output : 1j


"""
Integer :
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
"""
a = 1
b = 35656222554887711
c = -3255522
print((a))	# Output : 1
print((b))	# Output : 35656222554887711
print((c))	# Output : -3255522


"""
Float :
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
"""
d = 1.10
e = 1.0
f = -35.59
print((d)) # Output : 1.1
print((e)) # Output : 1.0
print((f)) # Output : -35.59


"""
Float can also be scientific numbers with an "e" to indicate the power of 10.
"""
g = 35e3
h = 12E4
i = -87.7e100
print((g)) # Output : 35000.0
print((h)) # Output : 120000.0
print((i)) # Output : -8.77e+101



"""
Complex :
Complex numbers are written with a "j" as the imaginary part:
"""
j = 3+5j
k = 5j
l = -5j
print((j)) # Output : (3+5j)
print((k)) # Output : 5j
print((l)) # Output : (-0-5j)


"""
Type Conversion : Casting
You can convert from one type to another with the int(), float(), and complex() methods:
"""
m = 1    # int
n = 2.8  # float
o = 1j   # complex

#convert from int to float:
aa = float(m)

#convert from float to int:
bb = int(n)

#convert from int to complex:
cc = complex(o)

print(aa) # Output : 1.0
print(bb) # Output : 2
print(cc) # Output : 1j

print(type(aa)) # Output : <class 'float'>
print(type(bb)) # Output : <class 'int'>
print(type(cc)) # Output : <class 'complex'>

"""
Note: You cannot convert complex numbers into another number type.




Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

Import the random module, and display a random number between 1 and 9:
"""
import random
print(random.randrange(1, 10)) # Output : 1
