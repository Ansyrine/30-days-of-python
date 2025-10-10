## Exercises Day 8 - Dictionaries

# exercise 1. create an empty dictionary called dog
dog = {}

# exercise 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['colour'] = 'Brown'
dog['breed'] = 'husky'
dog['legs'] = 4
dog['age'] = 3
print(dog) # prints the dog dictionary

# exercise 3. Create a student dictionary and add first_name, last_name,. gender, age, marital status, skills, country, city, and address as keys for the dictionary
student = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'gender': 'Female',
    'age': 22,
    'is_married': False,
    'skills': ['HTML', 'CSS', 'JavaScript, Rust'],
    'Country': 'Norway',
    'City': 'Oslo',
    'address': {
        'street': '456 Another St',
        'zip': '80085'
    }
}

# exercise 4. Get the length of the student dictionary
print(len(student)) 

# exercise 5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))

# exercise 6. Modify the skills values by adding one or two skills
student['skills'].append('Python')
student['skills'].append('C++')

# exercise 7. Get the dictionary keys as a list
print(student.keys())

# exercise 8. Get the dictionary values as a list
print(student.values())

# exercise 9. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print(student_items)

# exercise 10. Delete one of the items in the dictionary
del student['age']
print(student)

# exercise 11. Delete one of the dictionaries
del dog
# print(dog) # this will raise an error since the dog dictionary has been deleted