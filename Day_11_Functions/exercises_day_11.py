## Exercise level 1

#1. declare a function add_two_numbers. it takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 5))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area
print(area_of_circle(5))

#3. write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. if not do give a reasonable feedback.
def add_all_nums(*args):
    for arg in args:
        if not isinstance(arg, (int,float)):
            return f'error all arguments must be numbers. {arg} is not a number'
    return sum(args)

print(add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(1.5, 2.5, 3.5))
print(add_all_nums(1, 'hello', 3)) # should give an error message

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f
print(convert_celsius_to_fahrenheit(0))
print(convert_celsius_to_fahrenheit(100))

#5. write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower() # convert to lowercase to make it case insensitive
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'
print(check_season('March'))
print(check_season('august'))
print(check_season('Hello')) # should give invalid month

#6. write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'undefined (vertical line)'
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(1, 2, 3, 4))
print(calculate_slope(2, 3, 2, 5)) # should give undefined
print(calculate_slope(1, 3, 17, 30))

# 7. quadratic equation is calculated as follows ax^2 + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath # to handle complex numbers
def solve_quadratic_eqn(a, b, c):
    d = (b**2) - (4*a*c) # discriminant
    sol1 = (-b + cmath.sqrt(d)) / (2*a) 
    sol2 = (-b - cmath.sqrt(d)) / (2*a)
    return (sol1, sol2)
print(solve_quadratic_eqn(1, -3, 2)) # should return (2, 1)
print(solve_quadratic_eqn(1, 2, 5)) # should return complex solutions

#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)

print_list([1, 2, 3, 4, 5])
print_list(['apple', 'banana', 'cherry'])
print_list([]) 

#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reversed_arr = []
    for item in arr:
        reversed_arr.insert(0, item)
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(['a', 'b', 'c']))

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized_lst = []
    for item in lst:
        if isinstance(item, str):
            capitalized_lst.append(item.capitalize())
        else:
            capitalized_lst.append(item)
    return capitalized_lst
print(capitalize_list_items(['apple', 'banana', 'cherry']))
print(capitalize_list_items(['hello', 'world', 123])) # should handle non-string items

#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst
food_stuff = ['apple', 'banana', 'cherry']
print(add_item(food_stuff, 'orange'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

#12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
        return lst
    else:
        return f'Item {item} not found in list'
food_stuff = ['apple', 'banana', 'cherry']
print(remove_item(food_stuff, 'banana'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 5)) # should give item not found message

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    if n < 1:
        return 0
    return sum(range(1, n + 1))
print(sum_of_numbers(5)) # should return 15 (1+2+3+4+5)
print(sum_of_numbers(10)) # should return 55
print(sum_of_numbers(100)) # should return 5050

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    if n < 1:
        return 0
    return sum(i for i in range(1, n + 1) if i % 2 != 0)
print(sum_of_odds(5)) # should return 9 (1+3+5)
print(sum_of_odds(10)) # should return 25 (1+3+5+7+9)

#15. Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_evens (n):
    if n < 1:
        return 0
    return sum(i for i in range(1, n + 1) if i % 2 == 0)
print(sum_of_evens(5)) # should return 6 (2+4)
print(sum_of_evens(10)) # should return 30 (2+4+6+8+10)

## Exercise: Level 2

# Declare a function named evens_and_odds. it takes a positive integer as parameter and it counts the number of evens and odds in the number.
def evens_and_odds(n):
    if n < 0:
        return 'Input must be a positive integer'
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = len([i for i in range(n + 1) if i % 2 != 0])
    return (evens, odds)
print(evens_and_odds(100)) # should return (51, 50)
print(evens_and_odds(50)) # should return (26, 25)

#2. call your function factorial, it takes a while number as a parameter and it return a factorial of the number
def factorial(n):
    if n < 0:
        return 'input must be a non-negative integer' 
    if n == 0 or n == 1: # base case
        return 1
    return n * factorial (n - 1) # recursive case
print(factorial(5)) # should return 120

#3. call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if param:
        return False
    else:
        return True
print(is_empty([])) # should return True
print(is_empty([1, 2, 3])) # should return False

#4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

import statistics
import math
from collections import Counter

def calculate_mean(lst):
    """Calculate the mean (average) of a list"""
    if not lst:
        return 0
    return sum(lst) / len(lst)

def calculate_median(lst):
    """Calculate the median (middle value) of a list"""
    if not lst:
        return 0
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

def calculate_mode(lst):
    """Calculate the mode (most frequent value) of a list"""
    if not lst:
        return None
    counter = Counter(lst)
    max_count = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes

def calculate_range(lst):
    """Calculate the range (difference between max and min) of a list"""
    if not lst:
        return 0
    return max(lst) - min(lst)

def calculate_variance(lst):
    """Calculate the variance of a list"""
    if len(lst) < 2:
        return 0
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    """Calculate the standard deviation of a list"""
    return math.sqrt(calculate_variance(lst))

# Test the functions
numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
print(f"Mean: {calculate_mean(numbers)}")           # 5.0
print(f"Median: {calculate_median(numbers)}")       # 5.5
print(f"Mode: {calculate_mode(numbers)}")           # 5
print(f"Range: {calculate_range(numbers)}")         # 8
print(f"Variance: {calculate_variance(numbers)}")   # 6.4
print(f"Std Dev: {calculate_std(numbers)}")         # 2.53

## Exercise: Level 3

#1. write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11)) # should return True
print(is_prime(15)) # should return False

#2. Write a functions which checks if all items are unique in the list.
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))
print(are_all_items_unique([1, 2, 3, 4, 5])) # should return True
print(are_all_items_unique([1, 2, 3, 4, 5, 3])) # should return False

#3. Write a function which checks if all the items of the list are of the same data type.
def are_all_items_the_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)
print(are_all_items_the_same_type([1, 2, 3, 4, 5])) # should return True
print(are_all_items_the_same_type([1, '2', 3, 4, 5])) # should return False
print(are_all_items_the_same_type([])) # should return True (empty list)

#4. Write a function which checks if a given list is a valid Python variable name.
import keyword
def is_valid_variable_name(name):
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True
print(is_valid_variable_name('my_var')) # should return True
print(is_valid_variable_name('2nd_var')) # should return False
print(is_valid_variable_name('for')) # should return False (keyword)