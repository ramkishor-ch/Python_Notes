"""
Decorators :
A decorator is a function that takes another function and extends the behavior of this function without explicitly modifying it. 
It is a very powerful tool that allows to add new functionality to an existing function.

There are 2 kinds of decorators:
    a. Function decoratos
    b. Class decorators

A function is decorated with the @ symbol:
    @my_decorator
    def my_function():
        pass
"""


# Function decorators:
# A decorator is a function that takes another function as argument, wraps its behaviour inside an inner function and returns the wrapped function.

def start_end_decorator(func):
    
    def wrapper():
        print('Start')  #extending functionality
        func()
        print('End')    #extending functionality
    return wrapper

def print_name():
    print('Alex')

# Now wrap the function by passing it as argument to the decorator function, assign it to itself -> Our function has extended behaviour!
print_name = start_end_decorator(print_name)
print_name()

"""
Output:
    Start
    Alex
    End
"""



# The decorator syntax:
# Instead of wrapping our function and asigning it to itself, we can achieve the same thing simply by decorating our function with an @.

def start_end_decorator(func):
    
    def wrapper():
        print('Start')  #extending functionality
        func()
        print('End')    #extending functionality
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

print_name()

"""
Output:
    Start
    Alex
    End
"""





# function arguments
# If our function has input arguments and we try to wrap it with our decorator above, 
# it will raise a TypeError since we have to call our function inside the wrapper with this arguments, too. 
# However, we can fix this by using *args and **kwargs in the inner function:

def start_end_decorator_2(func):
    
    def wrapper(*args, **kwargs):   # if *args is not added then error occurs
        print('Start')
        func(*args, **kwargs)       # if *args is not added then error occurs
        print('End')
    return wrapper

@start_end_decorator_2
def add_5(x):
    return x + 5

result = add_5(10)
print(result)

"""
Output:
    Start
    End
    None
"""



# Return values
# Note that in the example above
# we do not get the result back, so as next step we also have to return the value from our inner function:

def start_end_decorator_3(func):
    
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)      # created result
        print('End')
        return result                       # returning result
    return wrapper

@start_end_decorator_3
def add_5(x):
    return x + 5

result = add_5(10)
print(result)

"""
Output:
    Start
    End
    15
"""



# function identity?
# If we have a look at the name of our decorated function, and inspect it with the built-in help function, 
# we notice that Python thinks our function is now the wrapped inner function of the decorator function.

print(add_5.__name__)
help(add_5)
"""
Output:
wrapper
Help on function wrapper in module __main__:
wrapper(*args, **kwargs)
"""


#To fix this, use the functools.wraps decorator, which will preserve the information about the original function. 
# This is helpful for introspection purposes, i.e. the ability of an object to know about its own attributes at runtime:

import functools
def start_end_decorator_4(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_4
def add_5(x):
    return x + 5
result = add_5(10)
print(result)
print(add_5.__name__)
help(add_5)
"""
Output:
    Start
    End
    15
    add_5
    Help on function add_5 in module __main__:
    add_5(x)
"""


# Decorator function arguments :

# Note that functools.wraps is a decorator that takes an argument for itself. 
# We can think of this as 2 inner functions, so an inner function within an inner function. 
# Example: A repeat decorator that takes a number as input. Within this function, 

# we have the actual decorator function that wraps our function and extends its behaviour within another inner function. 
# In this case, it repeats the input function the given number of times.

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Name is : {name}")
    
greet('Ram')

"""
Output:
    Name is : Ram
    Name is : Ram
    Name is : Ram
    Name is : Ram
"""



# Nested Decorators :
# We can apply several decorators to a function by stacking them on top of each other. 
# The decorators are being executed in the order they are listed.

import functools
def start_end_decorator(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		print('Start')
		result = func(*args,**kwargs)
		print('End')
		return result
	return wrapper

# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator_4
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

# now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
say_hello(name='Hari')

"""
Output:
    Calling say_hello(name='Hari')
    Start
    Hello Hari
    End
    'say_hello' returned 'Hello Hari'
"""




"""

Class decorators :
We can also use a class as a decorator. Therefore, we have to implement the __call__() method to make our object callable. 
Class decorators are typically used to maintain a state, e.g. here we keep track of the number of times our function is executed. 
The __call__ method does essentially the same thing as the wrapper() method we have seen earlier. 
It adds some functionality, executes the function, and returns its result. 
Note that here we use functools.update_wrapper() instead of functools.wraps to preserve the information about our function.

"""
import functools

class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(num):
    print("Hello!")

say_hello(5)
say_hello(5)

"""
Output:
    Call 1 of 'say_hello'
    Hello!
    Call 2 of 'say_hello'
    Hello!
"""