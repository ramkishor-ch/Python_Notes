# Built-in Data Types :

# Variables can store data of different types.

# Python has the following data types built-in by default, in these categories:
    # Text Type:	    str
    # Numeric Types:	int, float, complex
    # Sequence Types:	list, tuple, range
    # Mapping Type:	    dict
    # Set Types:	    set, frozenset
    # Boolean Type:	    bool
    # Binary Types:	    bytes, bytearray, memoryview
    # None Type:	    NoneType


# Setting the Data Type : the data type is set when you assign a value to a variable:

# Example	                                    Data Type	
# x = "Hello World"	                            str	
# x = 20	                                    int	
# x = 20.5	                                    float	
# x = 1j	                                    complex	
# x = ["apple", "banana", "cherry"]	            list	
# x = ("apple", "banana", "cherry")	            tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	            dict	
# x = {"apple", "banana", "cherry"}	            set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	                                    bool	
# x = b"Hello"	                                bytes	
# x = bytearray(5)	                            bytearray	
# x = memoryview(bytes(5))	                    memoryview	
# x = None	                                    NoneType

# Program :
a = "Hello World"
b = 20
c = 20.5
d = 1j	                                        	
e = ["apple", "banana", "cherry"]	            	
f = ("apple", "banana", "cherry")	            	
g = range(6)		
h = {"name" : "John", "age" : 36}	            	
i = {"apple", "banana", "cherry"}	            	
j = frozenset({"apple", "banana", "cherry"})		
k = True	                                    	
l = b"Hello"	                                	
m = bytearray(5)	                            	
n = memoryview(bytes(5))	                    	
o = None	

#display x:
print(a)		# Output: Hello World
print(type(a)) 	#display the data type
print(b)		# Output: 20
print(c)		# Output: 20.5
print(d)		# Output: 1j
print(e)		# Output: ['apple', 'banana', 'cherry']
print(f)		# Output: ('apple', 'banana', 'cherry')
print(g)		# Output: range(0,6)
print(h)		# Output: {'name': 'John', 'age': 36}
print(i)		# Output: {'cherry', 'apple', 'banana'}
print(j)		# Output: frozenset({'cherry', 'apple', 'banana'})
print(k)		# Output: True
print(l)		# Output: b'Hello'
print(m)		# Output: bytearray(b'\x00\x00\x00\x00\x00')
print(n)		# Output: <memory at 0x1483e2dbda00>
print(o)		# Output: None



# Setting the Specific Data Type :
# If you want to specify the data type, you can use the following constructor functions:

# Example	                                       Data Type	
# x = str("Hello World")	                       str	
# x = int(20)	                                   int	
# x = float(20.5)	                               float	
# x = complex(1j)	                               complex	
# x = list(("apple", "banana", "cherry"))	       list	
# x = tuple(("apple", "banana", "cherry"))	       tuple	
# x = range(6)	                                   range	
# x = dict(name="John", age=36)	                   dict	
# x = set(("apple", "banana", "cherry"))	       set	
# x = frozenset(("apple", "banana", "cherry"))	   frozenset	
# x = bool(5)	                                   bool	
# x = bytes(5)	                                   bytes	
# x = bytearray(5)	                               bytearray	
# x = memoryview(bytes(5))	                       memoryview