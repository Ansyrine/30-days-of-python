# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)     # 3
print('subraction: ', 3 -1) # 2
print('Multiplication: ', 2 * 3) # 6
print('division: ', 6/2) # 3.0
print('division: ', 7/2) # 3.5
print('Floor division: ', 7//2) # 3
print('division without remainder', 7// 3) #2
print('modulus', 3%2) 
print('exponentiation: ', 2 ** 3) # 8

# floating numbers
print('floating point number: , Pi', 3.14)
print('floating point number: , gravity', 9.81)

#complex numbers
print('complex number: ', 1 + 1j) 
print('multiplaying complex numbers: ',(1 + 1j) * (1 - 1j))

# declaring the variable at the top first
a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 2 is an integer data type

# arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponent = a ** b

# i should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total) 
print('a - b = ', diff) 
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponent)

print('== Addition, Subraction, Multiplication, Division, Modulus ==')

# declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_two / num_one
remainder = num_two % num_one

# printing the values with label
print('total: ', total) 
print ('difference: ', diff)
print('product: ', product)
print('division: ', division)
print('remainder: ', remainder)

# Area of a circle
radius = 10 # radius of a circle
area_of_circle = 3.14 * radius ** 2 #two * sign means excponent or power
print('Area of a circle:', area_of_circle)

# calculating area of a rectangle
length = 10 
width = 20
area_of_rectangle = length * width
print('Area of a rectangle: ', area_of_rectangle)

# calculating a weight of an object mass
mass = 75 # in kg
gravity = 9.81 # in m/s^2
weight = mass * gravity
print(weight, 'N') 

# calculating the density of a liquid
mass = 75 # in kg
volume = 0.075 # in m^3
density = mass / volume # density formula
print(density, 'kg/m^3')

# Comparison Operators
print(3 > 2) # True, because 3 is greater than 2
print(3 >= 2) # True, because 3 is greater than 2
print(3 < 2) # False, because 3 is not less than 2
print(2 <= 3) # True, because 2 is less than 3
print(2 <= 3) # True, because 2 is less than 3
print(3 == 2) # False, because 3 is not equal to 2
print(3 != 2) # True, because 3 is not equal to 2
print(len('mango') == len('avocado')) # False 
print(len('mango') != len('avocado')) # True
print(len('mango') < len('avocado')) # True
print(len('milk') != len('meat')) # False
print(len('milk') == len('meat')) # True
print(len('tomato') == len('potato')) # True 
print(len('python') > len('dragon')) # False

# comparing something gives either a True or False result
print('True == True: ', True == True) # True
print('True == False: ', True == False) # False
print('False == False: ', False == False) # True

'''
    is: Returns true if both variables are the same object(x is y)
    is not: Returns true if both variables are not the same object(x is not y)
    in: Returns True if the queried list contains a certain item(x in y)
    not in: Returns True if the queried list doesn't have a certain item(x in y)
'''

print('1 is 1: ', 1 is 1) # True - because the data values are the same
print('1 is not 2: ', 1 is not 2) # True - because 1 is not 2
print('S in Sylas' 'S' in 'Sylas') # True - S is in Sylas
print('B in Sylas' 'B' in 'Sylas') # False - B is not in Sylas
print('coding' in 'coding for all') # True - coding is in coding for all
print('a in an:', 'a' in 'an') # True - a is in an
print('4 is 2 ** 2: ', 4 is 2 **2) # True - because 4 is equal to 2 ** 2

print( 3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 <3) # False - because both statements are false
print('True and True: ', True and True)
print( 3 > 2 or 4 > 3) # True - because both statements are true
print( 3 > 2 or 4 < 3) # True - because one of the statements is true
print( 3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False: ', True or False) 
print(not 3 > 2) # False - because 3 is greater than 2
print(not True) # False - Negation, the not operator turns true to false
print(not False) # True - Negation
print(not not True) # True - Double negation, the not operator turns false to true
print(not not False) # False - Double negation, the not operator turns true to false

age: int = 22
height: float = 1.87 # in meters
weight: complex = 45 + 16j 

# area of a triangle
base = float(input ('Enter base: ')) # base of the triangle
height = float(input ('Enter height: ')) # height of the triangle
area = float(0.5) * base * height # area of triangle formula
print(area) 

# perimeter of a triangle 
side_a = float(input('side a: ')) 
side_b = float(input('side b: '))
side_c = float(input('side c: '))
perimeter = side_a + side_b + side_c
print(perimeter)

# rectangle
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

# rectangle formula
area = length * width
perimeter = 2 * (length + width) 

#rectangle output
print('area of the rectangle:', area)
print('perimeter of the rectangle:', perimeter)

#radius of a circle
radius = float(input('Enter the radius of the circle: ')) 
pi = 3.14
area_of_circle = pi * radius ** 2
circumference = 2 * pi * radius

#circle radius output
print('Area of the circle:', area_of_circle)
print('Circumference of the circle:', circumference)

slope = 2
y_intercept = -2 
x_intercept = -y_intercept / slope  

print('slope of y = 2x - 2:', slope)
print('y-intercept:', y_intercept)
print('x-intercept:', x_intercept)
 
x1, y1 = 2, 2
x2, y2 = 6, 10 

slope_points = (y2 - y1) / (x2 - x1) 
print('slope between points (2,2) and (6,10):', slope_points)

import math
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('distance between points (2,2) and (6,10):', distance)

if slope == slope_points:
    print('the slopes are equal.')
else: 
    print('the slopes are not equal.')

for x in range(-5, 10):
    y = x**2 + 6*x + 9
    print(f'x = {x}, y = {y}')

    x_zero = -3
    y_zero = x_zero**2 + 6* x_zero + 9
    print(f'at x = {x_zero}, y = {y_zero}')

print(len('python') != len('dragon')) 
print('on' in 'python' and 'on' in 'dragon') 
print('jargon' in 'I hope this course is not full of jargon') 

text = 'python'
length = len(text)         
length_float = float(length)  
length_str = str(length_float)  

print('Length:', length)
print('As float:', length_float)    
print('As string:', length_str)

number = 8
if number % 2==0:
    print('Even')
else:
    print('Odd')

result = 7 // 3           
int_value = int(2.7)     

print(result == int_value) 

print(type('10') == type(10)) 

value = int(float('9.8'))  
print(value == 10) 

hours = int(input('enter hours: '))
hourly_wage = float(input('enter hourly wage: '))
weekly_salary = hours * hourly_wage
print('weekly salary:', weekly_salary)


years = int(input('enter number of years: '))
seconds_in_a_year = 365 * 24 * 60 * 60 
total_seconds = years * seconds_in_a_year
print('you have lived for', total_seconds, 'seconds.')

max_seconds = 100 * seconds_in_a_year
print('a person can live up to', max_seconds, 'seconds in 100 years.')

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
