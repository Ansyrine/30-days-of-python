## Tuples

'''
A tuple is a collection of different data types which is ordered and unchangeable (immutable).
    Tuples are written with round brackets, ().
Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable).
Unlike lists, tuple has a few methods.
These methods are:
tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
    operator: + : to join two or more tuples
'''

## Creating a tuple
# empty tuple
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# tuple with initial values
tp1 =('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

## Tuple length
# we can use the len() method to get the length of a tuple.
tp1 = ('item1', 'item2', 'item3')
len(tp1) # 3

## Accessing tuple items
# positive indexing Similar to the list data type we use positive or negative indexing to access tuple items.
# positive indexing starts from 0 to n-1 where n is the length of the tuple.
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) -1 
last_fruit = fruits[last_index] 
print(first_fruit, second_fruit, last_fruit) # banana orange lemon

# Negative indexing
# negative indexing starts from -1 to -n where n is the length of the tuple.
tpl = ('item1', 'item2', 'item3', 'item4')
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

## Slicing tuples
# we can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.

# range of positive indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4] # all items
all_items=tpl[0:] # all items
middle_two_items = tpl[1:3] # from index 1 to index 3 but not including index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4] # all items
all_fruits = fruits[0:] # all items
orange_mango = fruits[1:3] # from index 1 to index 3 but not including index 3
orange_to_the_rest = fruits[1:] # from index 1 to the end of the tuple

# range of negative indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:] # all items
middle_two_items = tpl[-3:-1] # from index -3 to index -1 but not including index (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[4:] # all items
orange_mango = fruits[-3:-1] # from index -3 to index -1 but not including index -3
orange_to_the_rest = fruits[-3:] # from index -3 to the end of the tuple

## Changing tuples to lists
# we can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl) # changing tuple to list

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits) # changing tuple to list
fruits[0] = 'apple' # type: ignore # changing the first item
print(fruits) # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits) # changing list back to tuple
print(fruits) # ('apple', 'orange', 'mango', 'lemon')

## Checking an item in a tuple
# we can check if an item exists or not in a tuple using in, it returns a boolean.
tpl = ('item1', 'item2', 'item3', 'item4')
print('item2' in tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
# fruits[0] = 'apple' # This will raise an error because tuples are immutable

## Joining tuples
# we can join two or more tuples using the + operator.
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print('fruits and vegetables:', fruits_and_vegetables) # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')

## Deleting Tuples
# it is not possible to remove a single item in a tuple but it is possible to delete the entire tuple itself using del. 
tpl1= ('item1', 'item2', 'item3')
del tpl1
# print(tpl1) # this will raise an error because the tuple no longer exists

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

