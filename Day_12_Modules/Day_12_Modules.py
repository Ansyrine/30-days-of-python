## Modules
''' 
What is a module
A module is a single file containing a set of codes or a set of functions which can be included to an application.
a module could be a file containing a single variable, a big function or a big code base.
'''

## Creating a module
# to create a module we write our codes in a python script and we save it as a .py file.
# for example we create a file named mymodule.py and we write the following code in it: 
# def generate_full_name(firstname, lastname):
#     return firstname + ' ' + lastname
# we save the file and now we have created a module named mymodule.py

## Importing a module
# to import the file we use the import keyword and the name of the file only.
# for example to import the mymodule.py file we write the following code:
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))

## import functions from a module
# we can have many functions in a file and we can import all the functions differently
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabeneh', 'Yetayeh'))
print(sum_two_nums(3, 5))
mass = 100
weight = mass * gravity
print(weight) # 981.0 N = kg m/s2
print(person['firstname']) # Asabeneh

## import functions from a module and renaming
# during importing we can rename the name of the module.
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabeneh', 'Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight) # 981.0 N = kg m/s2
print(p) # 250
print(p['firstname']) # Asabeneh

## Import built-in modules
# Python has many built-in modules which we can use in our applications.

## OS module
# using python os module it is possible to autimatically perform many operating system tasks.
# the os module in python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.
'import the module'
import os
'creating a directory'
# os.mkdir('directory_name')
'changing the current directory'
# os.chdir('path/to/directory_name')
'getting current working directory'
# os.getcwd()
'removing directory'
# os.rmdir('directory_name')

'''
sys module
the sys module provides functions and variables used to manipulate different parts of the python runtime environment.
function sys.argv returns a list of command line arguments passed to a python script. 
the item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

some useful sys commands:
# to exit sys
sys.exit()
# to know the largest integer variable it takes
sys.maxsize
# to know path environment
sys.path
# to know the version of python you are using
sys.version
'''

## statistics module
# the statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.
from statistics import * # type: ignore # all the statistic modules
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print('ages: ', ages)
print('mean of ages: ', mean(ages)) # 23.875
print('median of ages: ', median(ages)) # 24.0
print('mode of ages: ', mode(ages)) # 24
print('standard deviation of ages: ', stdev(ages)) # ~2.3

## math module
# module containing many mathematical operations and constants.
import math
print(math.pi) # 3.141592653589793, pi constant
print(math.sqrt(2)) # 1.4142135623730951, square root of 2
print(math.pow(2, 3)) # 8.0, 2 to the power of 3
print(math.floor(9.81)) # 9, rounding down the decimal number
print(math.ceil(9.81)) # 10, rounding up the decimal number
print(math.log10(100)) # 2.0, log with base 10

'''
now, we have imported the math module which contains lots of function which can help us to perform mathematical calculations.
to check what functions the module has got, we can use help(math), or dir(math). 
this will display the available functions in the module.
if we want to import only a specific function from the module we can use from math import function_name.
for example, if we want to import only the pi constant from the math module we can use: 
from math import pi.
it is also possible to import multiple functions at once like this:
from math import pi, sqrt, pow
but if we want to import all the function in math module we can use *.
When we import we can also rename the name of the function.
for example, if we want to rename the sqrt function we can do it like this:
from math import sqrt as square_root
'''

## string module
# a string module is a useful module for many purposes. for example, it has a collection of string constants, functions for changing case, checking the nature of the string and many more.
import string
print(string.ascii_letters) # all ascii letters (lowercase and uppercase): abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # all ascii digits: 0123456789
print(string.punctuation) # all ascii punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

## random module
# let us import random module which gives us a random number between 0 and 0.9999... the random module has lots of functions which can help us to get random numbers, choose random items from a list, shuffle items in a list and many more.
from random import random, randint
print(random()) # it will print a random number between 0 and 1
print(randint(5, 20)) # it will print a random integer between 5 and 20

