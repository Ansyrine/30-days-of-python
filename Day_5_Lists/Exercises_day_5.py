## Exercises

# exercise 1: declare an empty list
empty_list = [] 

# exercise 2: declare a list with more than 5 items
five_item_list = [0, 1, 2, 3, 4]

# exercise 3: find the length of the list
print(len(five_item_list))

# exercise 4: get the first, middle and last item of the list
first_item = five_item_list[0]
print(first_item) 
middle_item = five_item_list[2]
print(middle_item) 
last_item = five_item_list[-1]
print(last_item) 

# exercise 5: declare a list called mixed_data_types and put your (name, age, height, marital status, address)
mixed_data_types = ['Sylas', 22, 1.87, 'Single', 'England']

# exercise 6: declare a list variable named it_companies and assign initial values
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# exercise 7: print the list using print()
print(it_companies) 

# exercise 8: print the number of companies in the list
print('number of companies:', len(it_companies))

#exercise 9: print the first, middle and last company
print('first company:', it_companies[0])
print('middle company:', it_companies[3])
print('last company:', it_companies[-1])

# exercise 10: print the list after modifying one of the companies
it_companies[0] = 'Meta'
print('it_companies changed:', it_companies) 

# exercise 11: add a new company to the list
it_companies.extend(['Twitter'])
print('it companies extended:', it_companies)

# exercise 12: insert an IT company in the middle of the companies list
it_companies.insert(3, 'LinkedIn') # inserted at index 3
print('it companies inserted:', it_companies)

# exercise 13: change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper() 
print('it companies upper:', it_companies)

# exercise 14: join the it_companies with a string '#;  '
it_companies = '#; '.join(it_companies) 
print('it companies joined:', it_companies)

# exercise 15: check if a certain company exists in the it_companies list
print('Is Apple in the list?, ', 'Apple' in it_companies)

# exercise 16: sort the list using sort() method
it_companies = it_companies.split('#; ')
it_companies.sort()
print('it companies sorted:', it_companies)

# exercise 17: reverse the list in descending order using reverse() method
it_companies.reverse()
print('it companies reversed:', it_companies) 

# exercise 18: slice out the first 3 companies from the list
print('first 3 companies:', it_companies[:3])

# exercise 19: slice out the last 3 companies from the list
print('last 3 companies:', it_companies[-3:])

# exercise 20: slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
print('middle company:', it_companies[middle_index]) 

# exercise 21: remove the first IT company from the list
it_companies.pop(0)
print('first company removed:', it_companies)

# exercise 22: remove the middle IT company or companies from the list
it_companies.pop(middle_index -1) # -1 because we already removed one item
print('middle company removed:', it_companies)

# exercise 23: remove the last IT company from the list
it_companies.pop(-1)
print('last company removed:', it_companies)

# exercise 24: remove all IT companies from the list
it_companies.clear() 
print('all companies removed:', it_companies)

# exercise 25: destroy the IT companies list
del it_companies

# exercise 26: join the following lists:
front_end  = ['HTML', 'CSS', 'JS', 'React', 'Redux']
print('front end:', front_end)
back_end = ['Node','Express', 'MongoDB']
print('back end:', back_end)
full_stack = front_end + back_end
print('full stack:', full_stack)

# exercise 27: After joining the lists in exercise 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print('full stack modified:', full_stack)

## Exercises: Level 2
# exercise 1: the following is a list of 10 student ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sub exercise 1: sort the list and find the min and max age
ages.sort()
print('sorted ages:', ages) 
print('min age:', ages[0])
print('max age:', ages[-1])

# sub exercise 2: add the min age and the max age again to the list
ages.extend([ages[0], ages[-1]])
print('ages extended:', ages) 
ages.sort() 
print('ages re-sorted:', ages) 

# sub exercise 3: find the median age (one middle item or two middle items divided by two)
length = len(ages)
if length % 2 == 0: # even number of items
    median = (ages[length//2 - 1] + ages [length//2]) / 2
else: # odd number of items
    median = ages[length//2]
print('median age:', median)

# sub exercise 4: find the average age (sum of all items divided by their number)
average = sum(ages) / len(ages) 
print('average age:', average)

# sub exercise 5: find the range of the ages (max minus min)
age_range = ages[-1] - ages[0] 
print('age range:', age_range)

# sub exercise 6: compare the value of (min - average) and (max - average), use abs() method
min_avg_diff = abs(ages[0] - average)
max_avg_diff = abs(ages[-1] - average)
print('min-avg diff:', min_avg_diff) 
print('max-avg diff:', max_avg_diff)
if min_avg_diff > max_avg_diff:
    print('min-avg is greater')
elif max_avg_diff > min_avg_diff:
    print('max-avg is greater')

# exercise 7: find the middle country(ies) in the countries list
from countries_list import countries 
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = countries[middle_index]
print('middle country(ies):', middle_countries)

# exercise 8: divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries) % 2 == 0:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]
else: # odd number of items
    first_half = countries[:middle_index + 1]
    second_half = countries[middle_index + 1:]
    print('first half:', first_half)
print('second half:', second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] exercise 9: unpack the first three countries and the rest as scandic countries.
first, second, third, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print('first:', first)
print('second:', second)
print('third:', third)
print('scandic countries:', scandic_countries)

