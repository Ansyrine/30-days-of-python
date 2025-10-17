## Higher order functions
'''
in python functions are treated as first class citizens, allowing you to perform the following operations on functions:
- a function can take one or more functions as parameters
- a function can be returned as a result of another function
- a function can be modified
- a function can be assigned to a variable

Today we'll be covering:
1. handling functions as parameters
2. returning functions as return value from another functions
3. using python closures and decorators
'''
## Function as a parameter
def sum_numbers(nums): # a normal function
    return sum(nums) # a function using the built-in sum function

def higher_order_function(f, lst): # function as a parameter
    summation = f(lst) # calling the function passed as parameter
    return summation # returning the result
result= higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result) # Output: 15

## Function as a return value
def square(x): # square function
    return x ** 2 

def cube(x): # a cube function
    return x ** 3

def absolute(x): # an absolute function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function_result(type): # function returning another function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function_result('square') # getting the square function
print(result(3)) # 9  # type: ignore
result = higher_order_function_result('cube') # getting the cube function
print(result(3)) # 27  # type: ignore
result = higher_order_function_result('absolute') # getting the absolute function
print(result(-3)) # 3  # type: ignore

# you can see from the above example that the higher order function is returning different functions depending on the passed parameter

## Python closures
'''
Python allows a nested function to access the outer scope of the enclosing function.
This is known as a Closure.
Let us have a look at how closures work in python
in python, closure is created by nesting a function inside another encapsulating function and then returning the inner function.
'''
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten() # returning the inner function
print(closure_result(5)) # 15
print(closure_result(20)) # 30

## Python decorators
# a decorator is a design pattern in python that allows a user to add new functionality to an existing object without modifying its structure.
# decorators are usually called before the definition of a function you want to decorate.
# to create a decorater function, we need an outer function with an inner wrapper function.

# normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function): # decorator function
    def wrapper(): # inner wrapper function
        func = function() # calling the passed function
        make_uppercase = func.upper() # modifying the result
        return make_uppercase # returning the modified result
    return(wrapper) # returning the inner function
g = uppercase_decorator(greeting) # decorating the greeting function
print(g()) # WELCOME TO PYTHON

## let us implement the example above with a decorator
# this decorator function is a higher order function that takes a function as a parameter

def upper_case_decorator(function): # decorator function
    def wrapper(): # inner wrapper function
        func = function() # calling the passed function
        make_uppercase = func.upper() # modifying the result
        return make_uppercase # returning the modified result
    return wrapper # returning the inner function
@upper_case_decorator # using the decorator
def greetings(): # normal function
    return 'Welcome to Python' # function to be decorated
print(greetings()) # WELCOME TO PYTHON
# you can see that by using the @upper_case_decorator above the greetings function, we have decorated the greetings function without modifying its structure.

## Applying multiple decorators to a single function
# let us create another decorator to demonstrate how multiple decorators can be applied to a single function

# first decorator
def uppercase_decorator_one(function): # decorator function
    def wrapper(): # inner wrapper function
        func = function() # calling the passed function
        make_uppercase = func.upper() # modifying the result
        return make_uppercase  # returning the modified result
    return wrapper # returning the inner function

# second decorator
def split_string_decorator(function): # decorator function
    def wrapper(): # inner wrapper function
        func = function() # calling the passed function
        splitted_string = func.split() # modifying the result
        return splitted_string # returning the modified result
    
    return wrapper # returning the inner function

@split_string_decorator # applying the second decorator
@uppercase_decorator_one # order is important in this case - .upper function does not work on lists. # applying the first decorator
def welcome_message(): # normal function
    return ' Welcome to Python' # function to be decorated
print(welcome_message()) # ['WELCOME', 'TO', 'PYTHON']

# you can see that by using the @split_string_decorator and @uppercase_decorator above the welcome_message function, we have decorated the welcome_message function with two decorators without modifying its structure.

## Accepting parameters in decorator functions
# most of the time we need our functions to take parameters, so we might need to define our decorator that accepts parameters.
def decorator_with_parameters(function): # decorator function
    def wrapper_accepting_parameters(para1, para2, para3): # inner wrapper function accepting parameters
        function(para1, para2, para3) # calling the passed function with parameters
        print('I live in {}'.format(para3)) # modifying the result
    return wrapper_accepting_parameters # returning the inner function

@decorator_with_parameters # using the decorator
def print_full_name(first_name, last_name, country): # normal function
    print('I am {} {}. I love to teach.'.format(first_name, last_name)) # function to be decorated
    
print_full_name('Asabeneh', 'Yetayeh', 'Finland') # calling the decorated function

## Built-in higher order functions
# Some of the built-in higher order functions that we cover in this section include:
# - map()
# - filter()
# - reduce()
# Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

# python map function
# the map() function is a built in function that takes a function and iterable as parameters.

# use case 1
numbers = [1, 2, 3, 4, 5] # iterable
def squared(x): # normal function
    return x ** 2 # function to be passed as parameter
numbers_squared = map(squared, numbers) # using map function
print(list(numbers_squared)) # 1, 4, 9, 16, 25]
# lets apply it with the lambda function
numbers_squared = map(lambda x : x ** 2, numbers) # using map function with lambda
print(list(numbers_squared)) # [1, 4, 9, 16, 25] 

# use case 2
numbers_str = ['1', '2', '3', '4', '5'] # iterable
numbers_int = map(int, numbers_str) # using map function to convert string to integer
print(list(numbers_int)) # [1, 2, 3, 4, 5]

# use case 3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] # iterable

def change_to_upper(name): # normal function
    return name.upper() # function to be passed as parameter

names_upper_cased = map(change_to_upper, names) # using map function
print(list(names_upper_cased)) # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# lets apply it with the lambda function
names_upper_cased = map(lambda name: name.upper(), names) # using map function with lambda
print(list(names_upper_cased)) # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
# what map actually does is iterating over a list. for instance, it changes the names to upper case and returns a new list.

## Python - Filter function
# the filter() function calls the specified function which returns boolean for each item if the specified iterable(list). It filters the items that satisfy the filtering criteria. 

# use case 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # iterable

def is_even(num): # normal function
    if num % 2 == 0: # function to be passed as parameter
        return True
    return False 

even_numbers = filter(is_even, numbers) # using filter function
print(list(even_numbers)) # [2, 4, 6, 8, 10]

# lets apply it with the lambda function
even_numbers = filter(lambda num: num % 2 == 0, numbers) # using filter function with lambda
print(list(even_numbers)) # [2, 4, 6, 8, 10]

# use case 2
def is_odd(num): # normal function
    if num % 2 != 0: # function to be passed as parameter
        return True
    return False

odd_numbers = filter(is_odd, numbers) # using filter function
print(list(odd_numbers)) # [1, 3, 5, 7, 9]

# lets apply it with the lambda function
odd_numbers = filter(lambda num: num % 2 != 0, numbers) # using filter function with lambda
print(list(odd_numbers)) # [1, 3, 5, 7, 9]

# use case 3
# filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] # iterable
def is_name_long(name): # normal function
    if len(name) > 7: # function to be passed as parameter
        return True
    return False

long_names = filter(is_name_long, names) # using filter function
print(list(long_names)) # ['Asabeneh']

# lets apply it with the lambda function
long_names = filter(lambda name: len(name) > 7, names) # using filter function with lambda
print(list(long_names)) # ['Asabeneh']
# what filter actually does is iterating over a list. for instance, it filters the even numbers and returns a new list.

## Python - Reduce function
# the reduce() function is defined in the functools module and we should import it from this module. like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value.
# example
from functools import reduce # importing reduce function from functools module
numbers = [1, 2, 3, 4, 5] # iterable
def add_two_numbs(x, y): # nomral function
    return int(x) + int(y) # function to be passed as parameter

total = reduce(add_two_numbs, numbers) # using reduce function
print(total) # 15
