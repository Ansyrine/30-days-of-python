# Day 2 - 30 days of python programming challenge 

# Variables in Python
# A variable is a container for a value, which can be of various data types such as
first_name = 'Sylas'   
last_name = 'vear'
country = 'england'
age = '22'
city = 'clitheroe'
is_married = False
skills = ['Python', 'javas', 'c++', 'walking', 'quick learning', 'problem solving']
person_info = { 
    'firstname': 'Sylas',
    'lastname': 'vear',
    'country':'england',
    'city' : 'clitheroe'
}

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

# Printing the values stored in the variables
print('First name:', first_name) 
print('Firsdt name length:', len(first_name)) # using len() to get the length of a string
print('Last name:', last_name) 
print('Last name length:', len(last_name)) # using len() to get the length of a string
print('Country:', country) 
print('Country length:', len(country))  # using len() to get the length of a string
print('Age:', age) # age is a string here
print('City:', city) # city is a string here
print('City length:', len(city)) # using len() to get the length of a string
print('Is married:', is_married) # boolean value
print('Skills:', skills) # list of skills

first_name, last_name, country, age, is_married = 'Sylas', 'vear', 'england', 22, False # multiple variable declaration in one line
print(first_name, last_name, country, age, is_married) # printing multiple variables in one line
print('First name:', first_name) 
print('Last name:', last_name) 
print('Country: ', country) 
print('Age: ', age)

# Taking input from the user using input()
first_name = input('What is your name: ') # input function takes string as default
age = input ('How old are you? ') # input function takes string as default

print(first_name)
print(age)

# different data types in Python
# Let's declare variables with different data types
first_name = 'Sylas'   # string
last_name = 'vear'     # string
country = 'england'    # string
city = 'clitheroe'     # string
age = 22               # integer
is_married = False     # boolean
skills = ['Python', 'javas', 'c++', 'walking', 'quick learning', 'problem solving'] # list
person_info = { 
    'firstname': 'Sylas',
    'lastname': 'vear',
    'country':'england',
    'city' : 'clitheroe'
}                      # dictionary

# printing out types of the variables
print(type('sylas')) # string
print(type(first_name)) # string
print(type(10)) #integer
print(type(3.14)) #float
print(type(True)) #boolean
print(type([1, 2, 3])) #list
print(type({'name': 'sylas'})) # dictionary
print(type((1, 2))) # tuple
print(type(zip([1,2],[3,4]))) # zip

# int to float
num_int = 10
print('num_int', num_int) # 10
num_float = float(num_int)
print('num_float:', num_float) # 10.0

# float to int
gravity = 9.81
print(int(gravity)) # 9 # float to int, removes decimal points

# int to string
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

# string to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str)) # 10.6
num_int = int(num_float) 
print('num_int', int(num_int)) #10

# string to list
first_name = 'Sylas'
print(first_name) # Sylas
first_name_to_list = list(first_name) # converting string to list
print(first_name_to_list) # ['S', 'y', 'l', 'a', 's']

print(len(first_name) == len(last_name)) # compare the length of your first name and last name

num_one = 5
num_two = 4
total = num_one + num_two #addition
print('Total:', total)

diff = num_one - num_two #subraction
print('Difference:', diff)

product = num_one * num_two # multiplication
print('Product:', product) 

division = num_one / num_two # division
print('Division:', division)

remainder = num_two % num_one # modulus
print('Remainder:', remainder) 

exp = num_one ** num_two # exponential
print('Exponent:', exp) 

floor_division = num_one // num_two # floor division
print('floordivision:', floor_division)  # the floor division rounds down the result to the nearest whole number

radius = 30
area_of_circle = 3.14159 * radius **2 # area of a circle = pi * r^2
circum_of_circle = 2 * 3.14159 * radius # circumference of a circle = 2 * pi * r
print('Area of circle:', area_of_circle)
print('circumference of a circle:', circum_of_circle) 


# area with user input
user_radius = float(input('enter radius: ')) # input is string by default, we convert it to float
user_area = 3.14159 * user_radius ** 2 # area of a circle = pi * r^2
print('Area with user input:', user_area)

First_name = input('enter your first name: ') 
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ') 
