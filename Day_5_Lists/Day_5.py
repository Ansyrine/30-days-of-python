## in python we can create lists in two ways
# using list built-in function
lst = list()
empty_lst = list() # creates an empty list
print(len(empty_lst)) # 0

# or using square brackets
lst = [] # creates an empty list
empty_lst = []
print(len(empty_lst)) # 0

# lists with initial values we use len() to find the length of a list
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yogurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['Finland', 'Denmark', 'Sweden', 'Norway', 'Iceland']

# print the lists and its length
print('fruits:', fruits) 
print('Number of fruits:', len(fruits))
print('vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('animal_products:', animal_products)
print('Number of animal_products:', len(animal_products))
print('web_techs:', web_techs)
print('Number of web_techs:', len(web_techs))
print('countries:', countries)
print('Number of countries:', len(countries))

# lists can have items of different data types
lst = ['Sylas', 22, True, {'country': 'England', 'city': 'Clitheroe'}]
print(lst)
print(len(lst))

## accessing list items using positive indexing
# we access each item in a list using their index. A list index starts from 0 to n-1 where n is the number of items in the list
print(fruits) # ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item in the list
print(first_fruit) # banana
second_fruit = fruits[1] # we are accessing the second item in the list
print(second_fruit) # orange
last_fruit = fruits[3] 
print(last_fruit) # lemon
# last index
last_index = len(fruits) - 1 # 4 - 1 = 3
last_fruit = fruits[last_index]
print(last_fruit) 

## accessing list items using negative indexing
# negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item, and so on.
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4] # we are accessing the first item in the list
print(first_fruit) # banana
last_fruit = fruits[-1] # we are accessing the last item in the list
print(last_fruit) # lemon
second_last = fruits[-2] # we are accessing the second last item in the list


## unpacking list items
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst # unpacking the list items
print(first_item) # item1
print(second_item) # item2
print(third_item) # item3
print(rest) # ['item4', 'item5']

# first example
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit) # banana
print(second_fruit) # orange
print(third_fruit) # mango
print(rest) # ['lemon', 'lime', 'apple']

# second example
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second) 
print(third) 
print(rest) # [4, 5, 6, 7, 8, 9]
print(tenth) 

# third example about unpacking list
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia'] 
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg) 
print(sw)
print(scandic) # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)

## Slicing items from a list
# positive indexing: we can specify a range of positive indexes by specifying the start, end, and step, the return value will be a new list
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
print(all_fruits)
# this will also give the same result as above
all_fruits = fruits[0:] # it returns all the fruits
print(all_fruits)
orange_and_mango = fruits[1:3] # it returns items starting from index 1 to index 3 but not including index 3
print(orange_and_mango)
orange_mango_lemon = fruits[1:] # it returns items starting from index 1 to the end of the list
print(orange_mango_lemon)
banana_mango = fruits [::2] # it returns every second item from the list
print(banana_mango)

'''
it will always start from the index 0 and will go up to the end of the list taking every second item
it doesn't start from item at index 1 because the default starting index is 0
meaning it will take the item at index 0 then skip the item at index 1 and take the item at index 2 and so on
so a list like this ['banana', 'orange', 'mango', 'lemon'] will return ['banana', 'mango']
because it starts from index 0 (banana) then skips index 1 (orange) and takes index 2 (mango) then skips index 3 (lemon) 
and there are no more items left
'''

# negative indexing: we can specify a range of negative indexes by specifying the start, end, and step, the return value will be a new list
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
print(all_fruits)
orange_and_mango = fruits[-3:-1] # it returns items starting from index -3 to index -1 but not including index -1 it does not include the last item
print(orange_and_mango)
orange_mango_lemon = fruits[-3:] # it returns items starting from index -3 to the end of the list
print(orange_mango_lemon)
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order
print(reverse_fruits) # ['lemon', 'mango', 'orange', 'banana']
# it returns the list in reverse order starting from the last item to the first item

## Modifying lists
# list is a mutable or modifiable ordered collection of items, meaning we can change, add, remove items in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado' # changing the first item
print(fruits) # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple' # changing the second item
print(fruits) # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime' # changing the last item
print(fruits) # ['avocado', 'apple', 'mango', 'lime']

## checking items in a list
# we can use the 'in' keyword to check if an item exists in a list, it returns a boolean
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist) # True
does_exist = 'lime' in fruits
print(does_exist) # False

## Adding items to a list
# to add items to a list we can use append(), insert(), and extend() methods
# append(): adds an item to the end of the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple') # adding apple to the end of the list
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime') # adding lime to the end of the list
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']

# insert(): adds an item at the specified index
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.insert(2, 'apple') # inserting apple between orange and mango at index 2
print(fruits) # ['banana', 'orange', 'apple', 'mango', 'lemon', 'banana']
fruits.insert(3, 'lime') # inserting lime between apple and mango at index 3
print(fruits) # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon', 'banana']

# extend(): adds items of a list to the end of another list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.extend(['apple', 'lime']) # adding multiple items to the end of the list
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
fruits_two = ['kiwi', 'strawberry']
fruits.extend(fruits_two) # adding another list to the end of the list
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime', 'kiwi', 'strawberry']
# we can also use '+' operator to concatenate two lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = fruits + ['apple', 'lime'] # concatenating two lists
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
fruits_two = ['kiwi', 'strawberry']
fruits = fruits + fruits_two # concatenating two lists
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime', 'kiwi', 'strawberry']

## Removing items from a list
# to remove items from a list we can use remove(), pop(), and clear() methods
# remove(): removes the specified item from the list
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana') # it removes the first banana it finds
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
fruits.remove('lemon') # it removes lemon from the list
print(fruits) # ['orange', 'mango', 'banana']
# if the item to be removed does not exist it raises a ValueError
# fruits.remove('lime') # ValueError: list.remove(x): x not in list
# to avoid this we can check if the item exists in the list before removing it
if 'lime' in fruits:
    fruits.remove('lime')
else:
    print('item not found in the list')

# pop(): removes an item at the specified index and returns the removed item
fruits = ['banana', 'orange', 'mango', 'lemon']
removed_fruit = fruits.pop() # it removes the last item from the list
print(removed_fruit) # lemon
print(fruits) # ['banana', 'orange', 'mango']
removed_fruit = fruits.pop(1) # it removes the item at index 1
print(removed_fruit) # orange
print(fruits) # ['banana', 'mango']
# if the index to be removed does not exist it raises an IndexError
# removed_fruit = fruits.pop(5) # IndexError: pop index out of range
# to avoid this we can check if the index is within the range of the list length
if len(fruits) > 5:
    removed_fruit = fruits.pop(5)
else:
    print('index out of range')

# clear(): removes all items from the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear() # it removes all items from the list
print(fruits) # []

## removing items using del
# the del keyword removes the specified index and it can also be used to delete items within index range. it can also delete the list entirely
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime'] 
del fruits[0] # it removes the first item from the list
print(fruits) # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1] # it removes the second item from the list
print(fruits) # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3] # it removes items from index 1 to index 3 but not including index 3
print(fruits) # ['orange', 'lime']
# del fruits  #it deletes the entire list
# print(fruits) # NameError: name 'fruits' is not defined
# to avoid this we can check if the list exists before printing it
if 'fruits' in locals():
    print(fruits)
else:
    print('list not found')

## copying a list
''' 
it is possible to copy a list by reassigning it to another variable but this is not a correct way of copying a list
because when we change the copied list it also changes the original list   
fruits = ['banana', 'orange', 'mango', 'lemon']
copied_fruits = fruits # this is not a correct way of copying a list
print(copied_fruits) # ['banana', 'orange', 'mango', 'lemon']
copied_fruits.append('lime')
print(copied_fruits) # ['banana', 'orange', 'mango', 'lemon', 'lime']
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'lime']
because both variables point to the same list in memory
to correctly copy a list we can use the copy() method or the list() function or slicing
'''

# using copy() method
fruits = ['banana', 'orange', 'mango', 'lemon']
copied_fruits = fruits.copy() # this is the correct way of copying a list
print(copied_fruits) # ['banana', 'orange', 'mango', 'lemon']
copied_fruits.append('lime') # adding lime to the copied list
print(copied_fruits) # ['banana', 'orange', 'mango', 'lemon', 'lime']
print(fruits) # ['banana', 'orange', 'mango', 'lemon']
# the original list remains unchanged

# using list() function
fruits = ['banana', 'orange', 'mango', 'lemon']
copied_fruits = list(fruits) # this is the correct way of copying a list
print(copied_fruits) # ['banana', 'orange', 'mango', 'lemon']
copied_fruits.append('lime') # adding lime to the copied list
print(copied_fruits) # ['banana', 'orange', 'mango', 'lemon', 'lime']
print(fruits) # ['banana', 'orange', 'mango', 'lemon'
# the original list remains unchanged

## Joining lists
#there are several ways to join, or concatenate, tho or more lists in python

# plus operator (+) 
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables 
print(fruits_and_vegetables) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# joining using extend() method. The extend() method modifies the original list by adding items from another list to it
num1 =[0, 1, 2, 3] 
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # [0, 1, 2, 3, 4, 5, 6]
print('num2 list remains unchanged:', num2) # [4, 5, 6]

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# zero and positive_numbers lists remain unchanged
print('Zero list remains unchanged:', zero) # [0]
print('Positive numbers list remains unchanged:', positive_numbers) # [1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('fruits and vegetables:', fruits) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print('vegetables list remains unchanged:', vegetables) # ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

## counting items in a list
# The count() method returns the number of times an item appears in a list:
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange')) # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24)) # 3
 
 ## finding index of an item
# The index() method returns the index of the first occurrence of the specified item in a list:
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange')) # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) # 2, the first occurrence 

## reversing a list
# the reverse() method reverses the order of the items in the list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [220, 198, 245, 257, 263, 294, 233, 224]
ages.reverse()
print(ages) # [224, 233, 294, 263, 257, 245, 198, 220]

## sorting list items
''' 
to sort lists we can use sort() method or sorted() built-in functions. 
The sort() method reorders the list items in ascending order and modifies the original list.
if an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

The sorted() function returns a new sorted list from the items in an iterable
(list, tuple, dictionary, etc.) 
and does not modify the original list.
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort() # it sorts the list in ascending order
print(fruits) # ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True) # it sorts the list in descending order
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort() 
print(ages) # [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True) 
print(ages) # [26, 25, 25, 24, 24, 24, 22, 19]
