## List Comprehension
# List comprehension is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.
# for instance if you want to change a string to a list of characters. You can use a couple of methods.
# Method 1: Using list() function
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

# method 2: list comprehension
lst = [i for i in language]
print(type(lst))
print(lst)

# Method 3: generating numbers
numbers = [i for i in range(11)]
print(numbers)

# method 4: it is also possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)

# method 5: making a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)

# list comprehension can be combined with if expressions

# generating a list of even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

# generating a list of odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# filtering numbers
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers) # [4, 6, 8, 10]

# flattening a three dimensional array using list comprehension
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Lambda function
'''
it can take any number of arguments, but can only have one expression. 
we need it when we want to write an anonymous function inside another function.

creating a lambda function
to create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression.
Lambda function does not use return but it explicitly returns the expression.
# syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
'''

# named function
def add_two_nums(a, b):
    return a + b
print(add_two_nums(3, 5))

# using lambda for the above function
add_two_nums = lambda a, b: a + b
print(add_two_nums(4, 7)) # 11

# self invoking lambda function
print((lambda a, b: a + b)(6, 7)) # 13

square = lambda x : x ** 2
print(square(5)) # 25
cube = lambda x : x ** 3
print(cube(5)) # 125

# multiple variables
multiple_variable = lambda x, y, z: x ** 2 - 3 * y + 4 * z
print(multiple_variable(5, 3, 4)) # 32

## using lambda function inside another function
def power(x):
    return lambda n : x ** n
cube = power(5)(3)
print(cube) # 125
two_power_of_five = power(2)(5)
print(two_power_of_five) # 32
