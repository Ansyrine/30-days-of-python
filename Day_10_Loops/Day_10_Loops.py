## Loops
'''
In order to handle repetitive tasks programming languages use loops. 
Python has the following loops:
1. while loop
2. for loop
'''
## While loop
# we used the reserved word while to make a while loop. it is used to execute a block of statements repeatedly until a given condition is satisfied.
# when the condition becomes false, the lines of code after the loop will be continued to be executed. 

count = 0
while count < 5:
    print(count)
    count = count + 1
# the above loop will print 0,1,2,3,4. when count becomes 5 the condition becomes false and the loop stops executing.
# in the above while loop, the condition becomes false when the count is 5. That is when the loop stops. if we are interested to run block of code once the condition is no longer true, we can use else.
count = 0
while count < 5:
    print(count)
    count = count + 1
else: 
    print('count is no longer less than 5', 'This is the count current count:', count)
# the above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. as a result 5 will be printed

## Break and continue - Part 1
# break: we use break when we like to get out of or stop the loop.
count = 0
while count < 5: 
    print(count) 
    count = count + 1
    if count == 3:
        break
# in the above loop when count is 3 the loop stops executing and we get 0,1,2 as output.
# continue: with the continue statement we can skip the current iteration, and continue with the next:
count = 0 
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

# the above loop will print 0,1,2,4. when count is 3 the continue statement skips the print statement and goes to the next iteration.#

## For loop
# A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tupele, a dictionary, a set, or a string).
# for loop with list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number) # the numbers will be printed line by line, from 0 to 5

# for loop with string
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])
# the above loop will give the same result as the previous loop. range(len(language)) gives a sequence of numbers from 0 to the length of the string. in this case it is from 0 to 5. then we access each letter using indexing.

# for loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers: 
    print(number)

# for loop with dictionary looping through a dictionary gives you the key of the dictionary.
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)
# in the above loop we used items() method to get the key and value of the dictionary.

# for loop with set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
# in the above loop the companies will be printed in a random order, because sets are unordered data structure.

## Break and continue - part 2
# break: is still the one to use when we want to stop our loop before it's completion
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break
# the above loop will print 0,1,2,3 and stops when number is 3

# continue: we use continue when we want to skip some of the steps in the iteration fo the loop.
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    if number == 3:
        continue
    print('next number should be', number + 1) if number != 5 else print('loops end')
print('outside the loop') # this will always be printed because it doesn't have the same indentation as the for loop
# in the above loop when number is 3 the continue statement skips the print statement and goes to the next iteration. as a result we get 0,1,2,4,5

## Range function
'''
the range() function is used to generate a sequence of numbers within a given range.
the range(start, end, stop) takes three parameters: starting, ending and increment.
by default it starts from 0 and the increment is 1.
the range sequences needs at least one argument (end). creating a range with one argument means starting from 0 to end-1
'''
lst = list(range(14))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
st = set(range(1,14)) # 2 arguments indicate start and end of the sequence, the increment is set to 1 by default
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

lst = list(range(0,14,2))
print(lst) # [0, 2, 4, 6, 8, 10, 12]
# in the above range the sequence starts from 0 to 13 with an increment of 2
st = set(range(0,14,2))
print(st) # {0, 2, 4, 6, 8, 10, 12}

## Nested for loop
# we can use a for loop inside another for loop. the inner loop will be executed one time for each iteration of the outer loop.
for i in range(3): # outer loop
    print(f'outer loop iteration: {i}')
    for j in range(2): # inner loop
        print(f'  inner loop iteration: {j}')
# in the above loop for each iteration of the outer loop, the inner loop will be executed completely. as a result we get 6 iterations in total.

person = {
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
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
# in the above loop we used a nested loop to access the skills from the person dictionary.

## for else
# if we want to execute some message when the loop ends, we use else.
for number in range(6):
    print(number) # prints 0 to 5, not including 6
else: print('the loop stops at', number)

## pass
# in python when statement is required after semicolon, but we don't want to write or execute any code, we use pass.
for number in range(6):
    pass # we don't want to do anything, so we use pass
