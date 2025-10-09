# ## Sets

'''
Set is a collection of items.
The mathematics definition of a set can be applied to Python sets.
A set is a collection of unordered and un-indexed items.
In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
Sets are written with curly brackets, {}. 
A set can have different data types, but a set cannot have mutable items like lists, sets or dictionaries as its elements.
Once a set is created, we cannot change its items, but we can add or remove items.

Key things to know about sets:
 Order: is not preserved.
 Order can change between different executions of the code.
 Order can vary between python versions
 sets only guarantee uniqueness, not order.
'''

## Creating a set
# We use the set() built in function.
# empty set
st = set() # we cannot create an empty set using {}

# set with initial values
st = {'item1', 'item2', 'item3', 'item4'}

## Set length
# we can use the len() method to get the length of a set.
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits) # 4

## Checking an item
# we can use the 'in' keyword to check if an item exists in a set.
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('orange' in fruits) # True
print('pineapple' in fruits) # False

## Adding items to a set
# once a set is created we cannot change any items but we can add new items using the add() method.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('kiwi') # {'banana', 'orange', 'mango', 'lemon', 'kiwi'}
print(fruits)

# we can add multiple items using the update() method.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.update(['grape', 'apple']) # {'banana', 'orange', 'mango', 'lemon', 'grape', 'apple'}
print(fruits)
# the update() allows to add multiple items to a set. The update() takes a list argument.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables) 
print(fruits)

## Removing items from a set
# we can remove an item from a set using remove() method. If the item is not found remove() will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2') 

# the pop() method removes a random item from the list and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop() # it removes a random item
print(fruits)

# if we are interested in the removed item we can assign it to a variable.
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print('this item has been removed:', removed_item)

## Clearing items in a set
# If we want to clear or empty the set we use clear method
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

## Deleting a set
# we can delete the entire set using the del keyword.
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
# print(fruits) # will return NameError: name 'fruits' is not defined

## Converting a list to a set
# we can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved
lst = ['item1', 'item2', 'item3', 'item4', 'item2']
st = set(lst) # {'item1', 'item2', 'item3', 'item4'}
print(st) 

## Joining sets 
# we can join two sets using the union() or update() method. 
# Union this method returns a new set and it doesn't change the original sets.
st1 = {'item', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) # {'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8'}
print(st3)

# Update this method doesn't return any value it just adds the items in the second set to the first set.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)
print(st1) # {'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8'}

## Finding intersection items
# intersection returns a set of items which are in both sets
st1 = {'item1', 'item2', 'common denominator', 'item4'}
st2 = {'item5', 'common denominator', 'item7', 'item8'}
print(st1.intersection(st2)) # {'common denominator'}

## checking subset and superset
'''
A set can be subset or super set of other sets. 
A set is a subset of another set if all items of the first set are in the second set. 
A set is a super set of another set if it has all items of the other set.
'''

# checking subset
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item4'}
print(st2.issubset(st1)) # True
print(st2.issuperset(st1)) # False

# checking super set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item4', 'item2', 'item3', 'item5'}
print(st2.issuperset(st1)) # True
print(st2.issubset(st1)) # False

## Checking the difference between two sets
# the difference() method returns the difference between two sets.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10} 
odd_numbers = whole_numbers.difference(even_numbers)
print(odd_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
unique_letters = python.difference(dragon)
print(unique_letters) # {'p', 'y', 't', 'h'}
unique_letters = dragon.difference(python)
print(unique_letters) # {'d', 'r', 'a', 'g'}

## Finding symmetric difference between two sets
# it returns the symmetric difference between two sets.
# it means that it returns a set that contains all items from both sets, except items that are present in both sets.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
symmetric_difference = whole_numbers.symmetric_difference(some_numbers)
print(symmetric_difference) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
symmetric_difference = python.symmetric_difference(dragon)
print(symmetric_difference) # {'p', 'y', 't', 'h', 'd', 'r', 'a', 'g'}

## Joining sets
# if two sets do not have have a common item or items we call them disjoint sets. 
# we can check if two sets are joint or disjoint using isdisjoint() method.
even_numbers = {0, 2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9,}
all_numbers = even_numbers.isdisjoint(odd_numbers) # True
print(all_numbers)

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
are_disjoint = python.isdisjoint(dragon) # False
print(are_disjoint) # they are not disjoint because they have common items 'o' and 'n'
