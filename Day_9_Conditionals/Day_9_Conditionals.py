## Conditionals
'''
By default, statements in pthon script are executed sequentially from top to bottom.
if the processing logic require so, the sequential flow of execution can be altered in two ways:
Conditional execution: a block of one or more statements will be executed if a certain expression is true
Repetitive execution: a block of one or more statements will be repetitevly executed as long as a certain expression is true
in this section we will cover if, else, elif statements.
the comparison and logical operators we learned in previous sections will be useful here.
'''

## If condition
# in python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon:
a = 3
if a > 0: 
    print('A is a positive number') # this line is executed only if the condition is true
# as you can see in the example above, 3 is greater than 0. The condition was true and the block code was executed. 
# however, if the condition is false we do not see the result. in order to see the result of the falsy condition, we should have another block, which is going to be else

## if else
# if condition is true the first block will be executed if not the else condition will fun. 

a = 3 
if a < 0: 
    print('A is a negative number')
else: 
    print( 'A is a positive number') # this line is executed because the condition is false
# The condition above proves falce, therefore the else block was executed. How about if our condition is more than two? We could use elif

## if elif else
# we use elif to check multiple conditions.
a = 0 
if a > 0:
    print('A is a positive number')
elif a <0: 
    print('A is a negative number')
else: 
    print('A is zero') # this line is executed because the condition is false and elif condition is also false

# shorthand # code if condition else code
a = 3
print('A is a positive number') if a > 0 else print('A is a negative number') if a < 0 else print('A is zero')

## nested conditions 
# conditions can be nested. Meaning you can have an if else statement inside another if else statement
a = 0
if a > 0: 
    if a % 2 == 0: 
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number') 
    # we can avoid nested conditions by using logical operator and.

## if condition and logical operators
a = 0
if a > 0 and a % 2 == 0:
    print(' A is an even and positive integer')
elif a > 0 and a % 2 != 0: 
    print('A is a positive and odd integer')
elif a == 0:
    print('A is zero')
else: 
    print('A is negative')

## if and or logical operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')
# in the example above, the user is not admin and the access level is not greater than or equal to 4. Therefore the condition is false and access is denied.
