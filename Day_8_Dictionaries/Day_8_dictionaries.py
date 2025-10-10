## Dictionaries 
# a dictionary is a collection of unordered, modificable(mutable) and paired (key:value) data types

## Creating a dictionary
# to create a dictionary we use curly brackets, {} or the dict() function
empty_dict = {}
# or
# dictionary with data values
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# an example would be
person = {
    'first_name': 'John',
    'last_name': 'Doe', 
    'age': 30,
    'country': 'USA',
    'is_married': False,
    'skills': ['Python', 'JavaScript', 'C++'],
    'address': {
        'street': '123 Main St',
        'city': 'New York', 
        'zip': '10001'
    }
}
print(person) # prints the whole dictionary
print(len(person)) # prints the number of key:value pairs in the dictionary

## Accessing items in a dictionary
# We can access dictionary items by referring to its key name.
print(person['first_name']) # prints 'John'
print(person.get('age')) # prints 30
print(person['address']['city']) # prints 'New York'
print(person.get('skills')) # prints ['Python', 'JavaScript', 'C++']
print(person['skills'][0]) # prints 'Python
# if we try to access a key that doesn't exist, it will raise a KeyError
print(person.get('middle_name')) # prints None

## Adding items to a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe', 
    'age': 30,
    'country': 'USA',
    'is_married': False,
    'skills': ['Python', 'JavaScript', 'C++'],
    'address': {
        'street': '123 Main St',
        'city': 'New York', 
        'zip': '10001'
    }
}
person['job_title'] = 'Software Engineer' # adds a new key:value pair to the dictionary
person['skills'].append('Java') # adds Java to the skills list
print(person) # prints the updated dictionary
person['address']['country'] = 'USA' # adds a new key:value pair to the nested dictionary
print(person)

## Modifying items in a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe', 
    'age': 30,
    'country': 'USA',
    'is_married': False,
    'skills': ['Python', 'JavaScript', 'C++'],
    'address': {
        'street': '123 Main St',
        'city': 'New York', 
        'zip': '10001'
    }
}
person['age'] = 31 # modifies the value of the key 'age'
person['skills'][0] = 'Python 3' # modifies the first item in the skills list
print (person) # prints the updated dictionary

## Checking keys in a dictionary
print('first_name' in person) # prints True
print('middle_name' in person) # prints False

## Removing Key and Value Pairs from a dictionary
# pop(key): removes the item with the specified key name
# popitem(): removes the last inserted item (in versions before Python 3.7, it removes an arbitrary item)
# del: removes the item with the specified key name or can delete the dictionary completely

person = {
    'first_name': 'John',
    'last_name': 'Doe', 
    'age': 30,
    'country': 'USA',
    'is_married': False,
    'skills': ['Python', 'JavaScript', 'C++'],
    'address': {
        'street': '123 Main St',
        'city': 'New York', 
        'zip': '10001'
    }
}
person.pop('age') # removes the key 'age' and its value
person.popitem() # removes the last inserted key:value pair which would be 'address' in this case
del person['skills'] # removes the key 'skills' and its value
print(person) # prints the updated dictionary

## Changing dictionary to a list of items
# the items() method changes dictionary to a list of tuples, each tuple contains a key:value pair
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items()) # prints dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

## Clearing a dictionary
# if we don't want the items in a dictionary we can clear them using clear() method
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.clear()) # prints {} which is an empty dictionary


## Deleting a dictionary
# if we do not use the dictionary we can delete it completely
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
del dct # deletes the dictionary
#print(dct) # this will raise a NameError since the dictionary has been deleted

## Copy a dictionary
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct. copy() # creates a copy of the dictionary
print(dct_copy) # prints {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

## Getting dictionary keys as a list
# the keys() method gives us all the keys of a dictionary as a list
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
keys = dct.keys() # gets all the keys of the dictionary
print(keys) # prints dict_keys(['key1', 'key2', 'key3', 'key4'])

## Getting dictionary values as a list
# the values() method gives us all the values of a dictionary as a list
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
values = dct.values() # gets all the values of the dictionary
print(values) # prints dict_values(['value1', 'value2', 'value3', 'value4'])