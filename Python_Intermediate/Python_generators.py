# Generators
# Generators are functions that can be paused and resumed on the fly, returning an object that can be iterated over.
# Unlike lists, they are lazy and thus produce items one at a time and only when asked. 
# So they are much more memory efficient when dealing with large datasets.
# A generator is defined like a normal function but with the yield statement instead of return.

def my_generator():
    yield 1
    yield 2
    yield 3

# Execution of a generator function :
# Calling the function does not execute it. 
# Instead, the function returns a generator object which is used to control execution. 
# Generator objects execute when next() is called. 
# When calling next() the first time, execution begins at the start of the function and continues until the first yield statement,
# where the value to the right of the statement is returned. 
# Subsequent calls to next() continue from the yield statement (and loop around) until another yield is reached. 
# If yield is not called because of a condition or the end is reached, a StopIteration exception is raised:

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# this will not print 'Starting'
cd = countdown(3)

# this will print 'Starting' and the first value
print(next(cd))

# will print the next values
print(next(cd))
print(next(cd))

# this will raise a StopIteration
# print(next(cd))   # error

"""
Output:
    Starting
    3
    2
    1
    Traceback (most recent call last):
    File "c:\Ramkishor.ch\D\GITHUBB\Functions_Python\Python_Notes\Python_Intermediate\Python_generators.py", line 38, in <module>
        print(next(cd))
            ^^^^^^^^
    StopIteration
"""


# for loop:
def countdown_2(num):
    # you can iterate over a generator object with a for in loop
    for x in cd:
        print(x)

cd = countdown_2(3)

"""
Output:
    Starting
    3
    2
    1
"""

# sum , sorted
def countdown_3(num):
    print('countdown_3')
    while num > 0:
        yield num
        num -= 1
cd = countdown_3(3)
sum_cd = sum(cd)
print(sum_cd)

cd = countdown_3(3)
sorted_cd = sorted(cd)
print(sorted_cd)
     
"""
Output:
    countdown_3
    6
    countdown_3
    [1, 2, 3]
"""



"""
Big advantage: Generators save memory!
Since the values are generated lazily, i.e. only when needed, it saves a lot of memory, especially when working with large data. 
Furthermore, we do not need to wait until all the elements have been generated before we start to use them.
"""
# without a generator, the complete sequence has to be stored here in a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")

"""
Output:
    499999500000
    8697464 bytes
"""

# with a generator, no additional sequence is needed to store the numbers
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")

"""
Output:
    499999500000
    120 bytes
"""



# Generator expressions :
# Just like list comprehensions, generators can be written in the same syntax except with parenthesis instead of square brackets. 
# Be careful not to mix them up, since generator expressions are often slower than list comprehensions because of the overhead of function calls

import sys

# generator expression
mygenerator = (i for i in range(100000) if i % 2 == 0)
# print(list(mygenerator))
print(sys.getsizeof(mygenerator))
# Output: 
# [0, 2, 4, 6, 8]
# 208

# list comprehension
mylist = [i for i in range(100000) if i % 2 == 0]
# print(list(mylist))
print(sys.getsizeof(mylist))
# Output: 
# [0, 2, 4, 6, 8] then 10 in range
# 444376
