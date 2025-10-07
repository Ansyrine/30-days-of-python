# # creating a string
letter = 'p'
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
practice_sentence = 'I hope you are enjoying 30 days of python challenge'
print(practice_sentence)
print(len(practice_sentence))

multiline_string = '''I am learning python to try something new
and learning is fun when using the right tools
this 30 days of python is definitely the right tools for me'''
print(multiline_string)

# string concatention connecting strings together
first_name ='Sylas'
last_name = 'Vear'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name)) # True
print(len(full_name))
 
# escape sequences in strings
'''
In Python and other programming languages \\ followed by a character is an escape sequence
\n: this makes a new line
\t: this means tab which is 8 spaces 
\\: this makes a single backslash
\': this makes a single quote
\": this makes a double quote
'''

print('I hope everyone is enjoying the Python Challenge. \nAre you?')
print('days\tTopics\texercises')
print('Day 1\t5\t5')
print('day 2\t6\t20')
print('day 3\t5\t23')
print('day 4\t1\t35')
print('this is a backslach symbol (\\)')

### string Formatting

## old style string formatting (% Operator)

'''
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string
which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".

%s = string (or any object with a string representation, like numbers)
%d = integers
%f = Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision (number of digits refers to the significant digits the decimal point)
'''

# strings only
first_name_one = 'Sylas'
last_name_one = 'Vear'
language = 'Python'
formated_string = 'I am %s %s. I am learning %s' %(first_name_one, last_name_one, language)
print(formated_string)


# strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string_one = 'The area of a circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after that that point
print(formated_string_one)

# strings only
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string_two = 'The following are python libraries:%s' %(python_libraries)
print(formated_string_two)

## New style string formatting (str.format)
'This formatting was introduced in Python version 3.'

first_name_two = 'Sylas'
last_name_two = 'Vear'
language_one = 'Python'
formated_string_three = 'I am {} {}. Im learning {}'.format(first_name_two, last_name_two, language_one)
print(formated_string_three)
a = 4 
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) #{:.2f} limits it to 2 numbers after the decmimal 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a //b))
print('{} ** {} = {}'.format(a, b, a **b))

# strings and numbers
radius_one = 10
pi_one = 3.14
area_one = pi * radius ** 2
formated_string_four = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string_four)

## String interpolation / f-strings (python 3.6)

# another new string formatting is string interpolation f - strings. strings that start with f and we can enject the data in their corresponding positions

a_one = 4
b_one = 3

print(f'{a_one} + {b_one} = {a_one + b_one}')
print(f'{a_one} - {b_one} = {a_one - b_one}')
print(f'{a_one} * {b_one} = {a_one * b_one}')
print(f'{a_one} / {b_one} = {a_one / b_one:.2f}')
print(f'{a_one} % {b_one} = {a_one % b_one}')
print(f'{a_one} // {b_one} = {a_one // b_one}')
print(f'{a_one} ** {b_one} = {a_one ** b_one}')

## Python strings as sequences of characters

# unpacking characters 
language_two = 'Python'
a_two,b_two,c,d,e,f = language # unpacking sequence characters into variables
print(a_two)
print(b_two)
print(c)
print(d)
print(e)
print(f)

## accessing characters in strings by index
# in programming counting starts from zero

language_three = 'Python'
first_letter = language_three[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) -1
last_letter = language[last_index]
print(last_letter)

# starting from the end
last_letter = language [-1]
print(last_letter)
second_last = language[-2]
print(second_last)

## slicing python strings
first_three = language_three[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) # pyt
last_three = language_three[3:6]
print(last_three) # hon
# another way to do this is
last_three_one = language_three[-3:]
print(last_three_one)
last_three_two = language_three [3:]
print(last_three_two) 
# both resulting in hon


# reversing a string
greeting_one = 'Hello, World!'
print(greeting_one[::-1]) # !dlroW ,olleH

# skipping characters while slicing
language_four = 'Python'
pto = language_four[0:6:2]
print(pto)

## String methods

# capitalize(): converts the first character of the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize())

# count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th'))# 2

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. it takes tab size argument
challenge_one = 'thirty\tdays\tof\tpython'
print(challenge_one.expandtabs())
print(challenge_one.expandtabs(10))

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
print(challenge.find('y')) # 5
print(challenge.find('th')) # 0

# rfind(): returns the index of the last occurrence of a substring, if not found returns -1
print(challenge.rfind('y'))
print(challenge.rfind('th'))

# format(): formats strings into a nicer output
first_name_three = 'Sylas'
last_name_three = 'Vear'
age = 22
job = 'looking for work'
country = 'england'
sentence_one = 'I am {} {}. I am {}. I am {} years old. I live in {}.'.format(first_name_three, last_name_three, job, age, country)
print(sentence_one) 

# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1) If the substring is not found it raises a value error
sub_string = 'da'
print(challenge.index(sub_string)) # 7
# print(challenge.index(sub_string, 9)) # error 

# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
print(challenge.rindex(sub_string)) # 7
# print (challenge.rindex(sub_string, 9)) #error
print(challenge.rindex('on', 8)) # 19

# isalnum(): Checks alphanumeric character
challenge_two = 'ThirtyDaysPython'
print(challenge_two.isalnum()) # True

challenge_three = '30DaysPython'
print(challenge_three.isalnum()) # True

# challenge = thirty days of python
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge_four = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha()L checks if all string elements are alphabet characters (a-z and A-Z)
print(challenge.isalpha()) # False, space is once again excluded

print(challenge_two.isalpha()) # True

num = '123'
print(num.isalpha()) # False

# isdecimal(): Checks if all characters in a string are decimal (0-9)
# challenge = 'thirty days of python'
print(challenge.isdecimal()) # False
# num = '123'
print(num.isdecimal()) # True
alphanum = '\u00B2'
print(alphanum.isdecimal()) # False

# isdigit(): Checks if all characters in a string are number (0-9 and some other unicode characters for numbers)
thirty_alt = 'Thirty'
print(thirty_alt.isdigit()) # False
thirty_number = '30' 
print(thirty_number.isdigit()) # True
# alphanum = '\u00B2'
print(alphanum.isdigit()) # True 

# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols like ½)
ten = '10'
print(ten.isnumeric()) # True
alphanum_one = '\u00BD' # ½
print(alphanum_one.isnumeric()) # True
ten_half = '10.5'
print(ten_half.isnumeric()) # false

# isidentifier(): checks for a valid identifier - it checks if a string is a valid variable name
# challenge_three = 30dayspython
print(challenge_three.isidentifier()) # False because it starts with a number
challenge_five = 'random_words_not_being_used'
print(challenge_five.isidentifier()) # True

# islower(): Checks if all alphabet characters in the string are lowercase
# challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge_six = 'Thirty days of Python'
print(challenge_six.islower()) # False

# isupper(): Checks if all alphabet characters in the string are uppercase
# challenge = 'thirty days of python'
print(challenge.isupper()) # False
challenge_seven = 'THIRTY DAYS OF PYTHON'
print(challenge_seven.isupper()) # True  

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React

# strip(): Removes all given characters starting from the beginning and end of the string 
# challenge = thirty days of python 
print(challenge.strip('noth')) # 'irty days of py'

# replace(): Replaces substring with a given string
# # challenge = 'thirty days of python 
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split(): Splits the string, using given string or space as a separator
# challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge_seven = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# title(): Returns a title cased string
# challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters 
# challenge = thirty days of python'
print(challenge.swapcase()) # THIRTY DAYS OF PYTHON
# challenge_seven = THIRTY DAYS OF PYTHON 
print(challenge_seven.swapcase()) # thirty days of python

# startswith(): checks if string starts with the specified string
# challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
# challenge_three = '30dayspython'
print(challenge_three.startswith('thirty')) # False
