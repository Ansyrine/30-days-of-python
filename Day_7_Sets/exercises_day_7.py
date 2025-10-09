# sets 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

## Exercises: level 1 
# 1. Find the lengtho of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Meta', 'LinkedIn', 'Snapchat'])
print(it_companies) 

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

# 5. What is the difference between remove and discard
'''
The remove() method removes the specified item from the set.
if the item to remove does not exist, remove() will raise an error.
The discard() method also removes the specified item from the set.
if the item to remove does not exist, discard() will NOT raise an error.
'''

## Exercises: level 2
# 1. Join A and B
C = A.union(B)
print(C)

A.update(B)
print(A) 

# 2. Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.intersection(B))

# 3. Is A subset of B
print(A.issubset(B)) # True

#4. Are A and B disjoint sets
print(A.isdisjoint(B)) # False

# 5. Join A with B and B with A
A.update(B) 
print(A)

B.update(A)
print(B)

# 6. What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.symmetric_difference(B)) # {27, 28}

# 7. Delete the sets completely
del A
del B

## Exercises: level 3
# 1. Convert the ages to a set and compare the length of the list and the set.
age_set = set(age) 
print(f'difference in length: {len(age) - len(age_set)}') #3

# 2. Explain the difference between the following data types: string, list, tuple and set.
'''
string: a sequence of characters enclosed in a single or double quotes. strings are immutable and cannot be changed once created.
list: a collection of items enclosed in square brackets. lists are mutable and can be changed after creation. lists can contain duplicate items.
tuple: a collection of items enclosed in parentheses. tuples are immutable and cannot be changed once created. tuples can contain duplicate items.
set: a collection of unordered and un-indexed items enclosed in curly brackets. we cannot change its items, but we can add or remove items. sets do not allow duplicate items.
'''

# 3 'I am a teacher and I love to inspire and teach people.' How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split() # split the sentence into words
unique_words = set(words) # convert the list of words to a set to get unique words
print(unique_words)
print(f'number of unique words: {len(unique_words)}') # 10
