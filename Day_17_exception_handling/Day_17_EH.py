## Exception handling
'''
python uses try and except to handle errors gracefully, a graceful exit(or graceful handling) of errors is a simple programming idiom
a program detects a serious error condition and 'exits gracefully', in a controlled manner as a result.
often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our applications more robust
the cause of an exception is often external to the program itself.
an example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device.
graceful handling of errors prevents our applications from crashing

if we use try and except in our program, then it will not raise errors in those blocks.

syntax:
try:
    code in this block if things go well
except:
    code in this block run if things go wrong

# example:
try:
    print(10 + '5')
except:
    print('something went wrong')

in the example above the second operand is a string. we could change it to a float or int to add it with the number to make it work. but without any changes, the second block, except, will be executed.
'''
from sys import exception


try:
    name = input('enter your name: ')
    year_born = input('Year you were born: ')
    age = 2025 - year_born
    print(f'You are {name}, and you are {age} years old.')
except:
    print('something went wrong')

'''
in the above example, the exception block will run and we do not know exactly the problem.
to analyze the problem, we can use the different error types with except.

in a following example, it will handle the error and will also tell us the kind of error raised.
'''
try:
    name = input('enter your name: ')
    year_born = input('Year you were born: ')
    age = 2025 - year_born 
    print(f'you are {name}, and you are {age} years old.')
except TypeError:
    print('type error occured')
except ValueError:
    print('value error occured')
except ZeroDivisionError:
    print('zero division error occured')

# in the code above the output is going to be TypeError. Now, lets add an additional block:

try:
    name = input('enter your name: ')
    year_born = input('Year you were born: ')
    age = 2025 - int(year_born) 
    print(f'you are {name}, and you are {age} years old.')
except TypeError:
    print('type error occured')
except ValueError:
    print('value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')

# it is also shorten the above code as follows:
try:
    name = input('enter your name: ')
    year_born = input('Year you were born: ')
    age = 2025 - int(year_born)
    print(f'you are {name}, and you are {age} years old.')
except Exception as e:
    print(e) 


## packing and unpacking arguments in python 
'''
we use two operators:
* for tuples
** for dictionaries
Let us take as an example below. it takes only arguments but we have list. we can unpack the list and changes to argument.
'''

## unpacking
# unpacking lists
# def sum_of_five_nums(a, b, c, d, e):
#    return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

# when we run this code, it raises an error, because this function takes numbers (not a list) as arguments. Let us unpack/destructure the list.
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst)) # this will work now

# we can also use unpacking in the range built-in function that expects a start and an end.
numbers = range(2, 7) # normal call with seperate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args) # call with arguments unpacked from a list
print(numbers) # range(2, 7)

# a list or a tuple can also be unpacked like this:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest) # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7,]
one, *middle, last = numbers
print( one, middle, last) # 1 [2, 3, 4, 5, 6] 7

# unpacking dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} years old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
    
## Packing
# sometimes we never know how many arguments need to be passed to a python function. we can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.

## Packing lists
def sum_all(*args): 
    s = 0 
    for i in args:
        s += i 
        return s
print(sum_all(1, 2, 3,)) # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

# packing dictionaries
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a a dict type
    # print(type(kwargs))
    # printing dictionary items
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs
print(packing_person_info(name='Asabeneh',
    country='Finland', city='Helsinki', age=250))

## Spreading in Python
# like in JavaScript, spreading is possible in python. let us check it in an example below:
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)
country_lst_one = ['finland', 'sweden', 'norway']
country_lst_two = ['denmark', 'iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

## enumerate
# if we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list.
for index, item in enumerate([20, 30, 40]):
    print(index, item)

## Zip
# sometimes we would like to combine lists when looping through them. See the example below:
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veggies = []
for f, v in zip(fruits, vegetables):
    fruits_and_veggies.append({'fruit':f, 'vegetables':v})

print(fruits_and_veggies)

## Exercise
# 1. names = names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
fin, sw, nor, den, ice, es, ru = names
nordic_countries = [fin, sw, nor, den, ice]
print(nordic_countries)
print(es)
print(ru)
