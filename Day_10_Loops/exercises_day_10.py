## Exercises

## Exercises: Level 1

#1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)
i = 0
while i<=10:
    print(i)
    i += 1


#2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)
    i = 10
    while i >= 0:
        print(i)
        i -= 1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
for i in range(1, 8):
    print('#' * i)


#4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()
    


# 5. Print the following pattern:

#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100

for I in range(11):
    print(f'{I} x {I} = {I*I}')



#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lst:
    print(item)

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)


#Use for loop to iterate from 0 to 100 and print only odd numbers
for I in range(101):
    if I % 2 != 0:
        print(I)

## Exercises: Level 2

#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.

# the sum of all numbers is 5050.
sum_all = 0
for i in range(101):
    sum_all += i 
    print('sum of all numbers is', sum_all) 


#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# The sum of all evens is 2550. And the sum of all odds is 2500.
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i%2 == 0:
        sum_evens += i
    else:
        sum_odds += i 
print('The sum of all evens is', sum_evens, '. And the sum of all odds is', sum_odds)

## Exercises: Level 3

#1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

from countries_list import countries
countries_with_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
print(countries_with_land)




#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0,fruit)
print(reversed_fruits)


#3. Go to the data folder and use the countries_data.py file.


#3.1. What are the total number of languages in the data
from countries_data import countries_data
all_language = []
for country in countries_data: 
    for language in country['languages']:
        if language not in all_language:
            all_language.append(language)
print('Total number of languages:', len(all_language))


#3.2. Find the ten most spoken languages from the data
language_count = {}
for country in countries_data:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language]= 1
            sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
            top_ten_languages = sorted_languages[:10]
print('Ten most spoken languages:', top_ten_languages)


#3.3. Find the 10 most populated countries in the world
country_population = {}
for country in countries_data: 
    country_population[country['name']] = country['population']
    sorted_countries = sorted(country_population.items(), key=lambda x: x[1], reverse=True)
    top_ten_populated_countries = sorted_countries[:10]
print('ten most populated countries:', top_ten_populated_countries)

