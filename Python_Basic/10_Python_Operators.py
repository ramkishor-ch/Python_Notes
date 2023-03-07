"""
Python Operators : Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:
    1. Arithmetic operators 
    2. Assignment operators
    3. Comparison operators
    4. Logical operators
    5. Identity operators
    6. Membership operators
    7. Bitwise operators

1. Arithmetic operators : It is used with numeric values to perform common mathematical operations:

Operator	Name	        Example
+	        Addition	    x + y	
-	        Subtraction	    x - y	
*	        Multiplication	x * y	
/	        Division	    x / y	
%	        Modulus	        x % y	
**	        Exponentiation	x ** y	
//	        Floor division	x // y

Program : """
x = 5
y = 3
print(x + y)  # Output : 8
print(x - y)  # Output : 2
print(x * y)  # Output : 15
print(x / y)  # Output : 1.6666666666666667
print(x % y)  # Output : 2
print(x ** y) # Output : 125
print(x // y) # Output : 1


"""
2. Python Assignment Operators : Assignment operators are used to assign values to variables:

Operator	Example	Same As	
=	        x = 5	x = 5	
+=	        x += 3	x = x + 3	
-=	        x -= 3	x = x - 3	
*=	        x *= 3	x = x * 3	
/=	        x /= 3	x = x / 3	
%=	        x %= 3	x = x % 3	
//=	        x //= 3	x = x // 3	
**=	        x **= 3	x = x ** 3	
&=	        x &= 3	x = x & 3	
|=	        x |= 3	x = x | 3	
^=	        x ^= 3	x = x ^ 3	
>>=	        x >>= 3	x = x >> 3	
<<=	        x <<= 3	x = x << 3

Program : """
x -= 3
print(x) # Output : 2

x = 5
x *= 3
print(x) # Output : 15

x = 5
x /= 3
print(x) # Output : 1.666

x = 5
x %= 3
print(x) # Output : 2

x = 5
x//=3
print(x) # Output : 1

x = 5
x **= 3
print(x) # Output : 125

x = 5
x &= 3
print(x) # Output : 1

x = 5
x |= 3
print(x) # Output : 7

x = 5
x ^= 3
print(x) # Output : 6

x = 5
x >>= 3
print(x) # Output : 0

x = 5
x <<= 3
print(x) # Output : 40


"""
3. Python Comparison Operators : It is used to compare two values:

Operator	Name	                    Example
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<       	Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y

Program : """
x = 5
y = 3
print(x == y) # Output : False
print(x != y) # Output : True
print(x > y) # Output : True
print(x < y) # Output : False
print(x >= y) # Output : True
print(x <= y) # Output : False


"""
4. Python Logical Operators : It is used to combine conditional statements:

Operator	Description                                 	        Example
and 	    Returns True if both statements are true	            x < 5 and  x < 10	
or	        Returns True if one of the statements is true	        x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

Program : """
x = 5
print(x > 3 and x < 10)		 # Output : True
print(x < 5 or x < 4)		 # Output : False
print(not(x < 5 and x < 10)) # Output : True


"""
5. Python Identity Operators : It is used to compare the objects, not if they are equal,
                               but if they are actually the same object, with the same memory location:

Operator	Description	                                            Example	
is 	        Returns True if both variables are the same object	    x is y	
is not	    Returns True if both variables are not the same object	x is not y

Program : """
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(x is not z) # returns False because z is the same object as x
print(x is not y) # returns True because x is not the same object as y, even if they have the same content
print(x != y) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


"""
6. Python Membership Operators : It is used to test if a sequence is presented in an object:

Operator	Description	                                                                        Example
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y

Program : """
x = ["apple", "banana"]

print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list


"""
7. Python Bitwise Operators : It is used to compare (binary) numbers:

Operator	Name	                Description	                                            Example
& 	        AND	                    Sets each bit to 1 if both bits are 1               	x & y	
|	        OR	                    Sets each bit to 1 if one of two bits is 1	            x | y	
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1	        x ^ y	
~	        NOT	                    Inverts all the bits	                                ~x	
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and 
                                    let the leftmost bits fall off	                        x << 2	
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in 
                                    from the left, and let the rightmost bits fall off	    x >> 2

Program : """
print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010    # Output
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


print(6 | 3)
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111    # Output
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101    # Output
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100   # Output

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""


print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100   # Output

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010   # Output

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


"""
8. Operator Precedence : It describes the order in which operations are performed.

The precedence order is described starting with the highest precedence at the top:

Operator	Description
()	        Parentheses	
**	        Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	    Addition and subtraction	
<<  >>	    Bitwise left and right shifts	
&	        Bitwise AND	
^	        Bitwise XOR	
|	        Bitwise OR	
==  !=  >  
>=  <  <=  
is  is not  
in  not in 	Comparisons, identity, and membership operators	
not	        Logical NOT	
and	        AND	
or	        OR

Example : """
print((6 + 3) - (6 + 3))
"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""

print(100 + 5 * 3)
"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

print(100 - 3 ** 3)
"""
Exponentiation has higher precedence than subtraction, and needs to be evaluated first.
The calculation above reads 100 - 27 = 73
"""

print(100 + ~3)
"""
Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + -4 = 96
"""

print(8 >> 4 - 2)
"""
Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
The calculation above reads 8 >> 2 = 2

More explanation:
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print(6 & 2 + 1)
"""
Bitwise AND has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 & 3 = 2

More explanation:
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""



print(6 ^ 2 + 1)
"""
Bitwise XOR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 ^ 3 = 5

More explanation:
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


print(6 | 2 + 1)
"""
Bitwise OR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 | 3 = 7

More explanation:
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


print(5 == 4 + 1)
"""
The "like" comparison has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 5 == 5 = True
"""


print(not 5 == 5)
"""
The logical NOT operator has a lower precedence than "like" comparison, and we need to calculate the comparison first.
The calculation above reads: not True = False
"""


print(1 or 2 and 3)
"""
The and operator has a higher precedence than or, and we need to calculate the and expression first.
The calculation above reads: 1 or 3 = 1
"""


print(4 or 5 + 10 or 8)
"""
The or operator has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads: 4 or 15 or 8 = 4
"""

# If two operators have the same precedence, the expression is evaluated from left to right.
print(5 + 4 - 7 + 3)
"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""





