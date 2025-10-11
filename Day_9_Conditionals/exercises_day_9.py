## Exercises

## exercises: level 1
# 1. Get user input using input('enter your age:'). if user is 18 or older, give feedback: 'You are old enough to drive' if below 18 give feedback to wait for the missing amount of years.

age = int(input('enter your age: '))
if age >= 18:
    print('You are old enough to drive')
elif age < 18:
    print(f'you need to wait {18 - age} years to be able to drive') 


'''
Compare the values of my_age and your_age using if … else. 
Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
'''
my_age = 22
your_age = int(input('enter your age: '))

if my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print(f'I am {diff} year older than you')
    else:
        print(f'I am {diff} years older than you')
elif my_age < your_age:
    diff = your_age - my_age
    if diff == 1:
        print(f'you are {diff} year older than me')
    else:
        print(f'you are {diff} years older than me')
elif my_age == your_age:
    print('we are the same age')


'''
3. get two numbers from the user using input prompt.
if a is greater than b return a is greater than b
if a is less than b return a is smaller than b
else a is equal to b
'''
a = int(input('enter number a: '))
b = int (input('enter number b: '))

if a > b: 
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
elif a == b:
    print(f'{a} is equal to {b}')


## Exercises: level 2
'''
1. write code that gives grade to students according to their scores:
80-100, A
70-89, B
60-69, C
50-59, D
40-49, F
'''
score = int(input('enter your score: '))
if 80 <= score <= 100:
    print('You got an A')
elif 70 <= score <= 79:
    print(' You got a B')
elif 60 <= score <= 69:
    print('You got a C')
elif 50 <= score <= 59:
    print('You got a D')
elif 0 <= score <= 49:
    print(' you got an F') 
else:
    print('score must be between 0 and 100') 

'''
2. Check if the season is autumn, winter, spring, or summer. 
if the user input is: September, October or November, the season is autumn.
if the user input is: December, January or February, the season is winter.
if the user input is: March, April or May, the season is spring
if the user input is: June, July or August, the season is summer
'''
month = input('enter month: ').capitalize()

if month in ['September', 'October', 'November']:
    print('the season is Autumn')
elif month in ['December', 'January', 'February']:
    print('the season is Winter')
elif month in ['March', 'April', 'May']:
    print('the season is Spring')
elif month in ['June', 'July', 'August']:
    print('the season is Summer')
else:
    print('Invalid month name')

'''
3. the following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
if a fruit doesn't exist in the list add the fruit to the list and print the modified list.
if the fruit exists print('that fruit already exists in the list')
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('enter a fruit: ').lower() 
if new_fruit in fruits:
    print('the fruit already exists in the list')
else:
    fruits.append(new_fruit)
    print(fruits)
    print('fruit added to the list')

## Exercises: level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
'''
1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
'''
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f'the middle skill is: {skills[middle_index]}')

'''
2. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
'''
if 'skills' in person:
    if 'Python' in person['skills']:
        print('the person has python skill')
    else:
        print('the person does not have python skill')

'''
3. If a person skills has only JavaScript and React, print('He is a front end developer'),
if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
else print('unknown title')
'''
if 'skills' in person:
    skills = person['skills']
    if skills == ['JavaScript', 'React']:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('unknown title')

'''
4. if the person is married and if he lives in Finland print the information in the following format:
Asabeneh Yetayeh lives in Finland. He is married.
'''
if person.get('is_married') and person.get('country') == 'Finland':
    print(f'{person.get('first_name')} {person.get('last_name')} lives in {person.get('country')} He is married.')
else:
    print('the person is either not married or does not live in Finland')

