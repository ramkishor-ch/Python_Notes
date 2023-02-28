"""
Itertools:
The Python itertools module is a collection of tools for handling iterators. 
Simply put, iterators are data types that can be used in a for loop. 
The most common iterator in Python is the list.

itertools: product, permutation, combinations, accumulate, groupby and infinite iterators

more information: https://docs.python.org/3/library/itertools.html
"""

"""
product() :
This tool computes the two sets product of input iterables.
"""
from itertools import product
a = [1,2]
b = [3,4]
pr=product(a,b)
print(list(pr)) #Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

c = [4,5]
d = [6]
py=product(c,d,repeat=2) 
print(list(py)) #Output: [(4, 6, 4, 6), (4, 6, 5, 6), (5, 6, 4, 6), (5, 6, 5, 6)]



"""
permutations() :
It successive length permutations of elements in an iterable, with all possible orderings, and no repeated elements.
"""
from itertools import permutations
a=[1,2,3]
perm=permutations(a)
print(list(perm)) #Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

permu=permutations(a,2)
print(list(permu)) #Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]



"""
combinations() and combinations_with_replacement() :
r-length tuples, in sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order. 
combinations() does not allow repeated elements, but combinations_with_replacement() does.
"""
from itertools import combinations, combinations_with_replacement
a=[1,2,3,4]
comb=combinations(a,2)
print(list(comb)) #Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb_wr=combinations_with_replacement(a,2) #same number to be repeated then use replacement function
print(list(comb_wr)) #Output: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]



"""
accumulate() :
Make an iterator that returns accumulated sums, or accumulated results of other binary functions.
"""
from itertools import accumulate
import operator 
a=[1,2,3,4]
acc=accumulate(a)
print(list(acc)) #Output: [1,3,6,10]

act=accumulate(a,func=operator.mul)
print(list(act)) #Output: [1, 2, 6, 24]

acv=accumulate(a,func=max)
print(list(acv)) #Output: [1, 2, 3, 4]



"""
groupby() :
Make an iterator that returns consecutive keys and groups from the iterable. 
The key is a function computing a key value for each element. 
If not specified or is None, key defaults to an identity function and returns the element unchanged. 
Generally, the iterable needs to already be sorted on the same key function.
"""
from itertools import groupby
def smaller_than_3(x):
	return x < 3

a = [1,2,3,4]
group_obj = groupby(a,key=smaller_than_3)  # lambda function: groupby(a, key=lambda x: x<3)
# if key is not provided in groupby function then it returns the object address
for key, value in group_obj:
	print(key, list(value))
	"""
    Output:
        True [1, 2]     
        False [3, 4]
    """

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))
    """
    Output:
    25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
    27 [{'name': 'Lisa', 'age': 27}]
    28 [{'name': 'Claire', 'age': 28}]  
    """

"""
Infinite iterators: count(), cycle(), repeat()
"""
from itertools import count, cycle, repeat
# count(x): count from x: x, x+1, x+2, x+3...
for i in count(10):
    print(i,end=" ")    # Output: 10 11 12 13
    if  i >= 13:    # without if condition the loop will be infinite
        break

# cycle(iterable) : cycle infinitely through an iterable
print("")
sum = 0
for i in cycle([1, 2, 3]):
    print(i,end=" ")   # Output: 1 2 3 1 2 3
    sum += i
    if sum >= 12:
        break

# repeat(x): repeat x infinitely or n times
print("")
for i in repeat("A", 3):
    print(i, end=" ") # Output: A A A


