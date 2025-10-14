## Functions
'''
Defining a Function
a function is a reusable block of code or programming statements designed to perform a certain task.
to define or declare a function, python provides the def keyword.
the function block of code is executed only if the function is called or invoked.
'''

## Declaring and calling a function
# when we make a function, we call it declaring a function. when we start using the it, we call it calling or invoking a function. function can be declared with or without parameters
'syntax:'
'''def function_name ():
    # block of code
    # block of code
    # optional return statement'''



## Function without parameters
# function can be declared without parameters.
def generate_full_name_one():
    first_name = 'Asabeneh' 
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

def add_two_numbers (): 
    num_one = 2
    num_two = 3
    total =num_one + num_two
    print(total)
    add_two_numbers() # calling a function

## Function returning a value - part 1
# functions can also return values, if a function does not have a return statement, the value of the function is none.
# from now on, we get a value from a function when we call the function and print it.
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_2_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_2_numbers())


## Function with parameters 
# in a function we can pass different data types (number, string, boolean, list, tuple, dictionary, or set) as a parameters
# single parameters: if our function takes a parameter we should call our function with an argument.

def greetings (name):
    message = name + ', welcome to python functions!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def sum_of_numbers (n):
    total = 0
    for i in range(n+1):
        total +=i
    print(total)
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# two parameter: a function may or may not have a parameter or parameters. a function may also have two or more parameters. If our function takes parameters we should call it with arguments. let us check a function with two parameters:
def generate_full_name_with_two_parameters (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name_with_two_parameters('Asabeneh', 'Yetayeh'))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + 'N'
    return weight
print(' weight of an object in newtons: ', weight_of_object(100, 9.81))

## Passing arguments with key and value
# if we pass the arguments with key and value, the order of the arguments does not matter.

# returning a string:
def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name
print_full_name(lastname='Yetayeh', firstname='Asabeneh')

# returning a number: 
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('age: ', calculate_age(birth_year=1819, current_year=2019))

# returning a boolean:
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True
    return False
print(is_even(10)) # True
print(is_even(7)) # False

# returning a list:
def find_even_numbers (n):
    evens = []
    for i in range(n +1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10)) # [0, 2, 4, 6, 8, 10]

## Function with default parameters
# Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.
def greetings_one (name= 'Peter'):
    message = name + ', welcome to python for everyone!'
    return message
print(greetings_one())
print(greetings_one('Asabeneh'))

## arbitrary number of arguments
# if we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(16, 43, 15, 7))

## default and arbitrary number of parameters in functions
def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('team-1', 'Asabeneh', 'Brook', 'David', 'Eyob')

## Function as a parameter of another function
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 9