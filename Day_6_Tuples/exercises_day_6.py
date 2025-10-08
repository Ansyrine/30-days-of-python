## Exercises: Level 1

# exercise 1: create an empty tuple
empty_tuple = ()

# exercise 2: create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Alice', 'Beth')
brothers = ('Charlie', 'David')

# exercise 3: join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings) # ('Alice', 'Beth', 'Charlie', 'David')

# exercise 4: How many siblings do you have?
print(len(siblings)) # 4

# exercise 5: modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Maggy', 'Devon')
print(family_members) # ('Alice', 'Beth', 'Charlie', 'David', 'Maggy', 'Devon')

## Exercises: Level 2

# exercise 1: Unpack siblings and parents from family_members
sister1, sister2, brother1, brother2, mother, father, = family_members
print(sister1) # Alice
print(brother2) # David
print(father) # Devon

# exercise 2: Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('carrot', 'potato', 'cabbage', 'onion', 'tomato') 
animal_products = ('milk', 'meat', 'eggs', 'cheese') 
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# exercise 3: Change the about food_stuff_tp tuple to a food_stuff_lst list
food_stuff_lst = list(food_stuff_tp)

# exercise 4: Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lst list.
middle_item = food_stuff_lst[len(food_stuff_lst)//2]
print(middle_item) # cabbage

# exercise 5: Slice out the first three items and the last three items from food_stuff_lst list
first_three = food_stuff_lst[:3]
last_three = food_stuff_lst[-3:]
print(first_three) # ['banana', 'orange', 'mango']
print(last_three) # ['milk', 'meat', 'eggs']

# exercise 6: Delete the food_stuff_tp tuple completely
del food_stuff_tp # tuple deleted

# exercise 7: Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('estonia' in nordic_countries) # False
print('iceland' in nordic_countries) # True
