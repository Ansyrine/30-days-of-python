### Exercises
## Exercise level 1
#1. explain the difference between map, filter, and reduce.
'''
- map applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).
- filter creates a list of elements for which a function returns true. It filters the elements based on a condition.
- reduce applies a rolling computation to sequential pairs of values in an iterable. It reduces the iterable to a single cumulative value.
'''
#2. explain the idfference between higher order function, closure and decorator.
'''
- A higher-order function is a function that can take other functions as arguments or return them as results.
- A closure is a nested function that captures the local variables from its enclosing scope, allowing it to remember those variables even when called outside that scope.
- A decorator is a special type of higher-order function that takes a function as input and returns a modified version of that function, often used to add functionality to the original function.
'''

#3. define a call function before map, filter, or reduce.
from os import remove


def call_function(func, iterable):
    return func(iterable)
# Example usage:
numbers = [1, 2, 3, 4, 5]
squared_numbers = call_function(lambda x: list(map(lambda n: n ** 2, x)), numbers)
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

#4. use loop to print each country in the countries list 
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

#5. use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name) 

#6. use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

## Exercise level 2
#1. Use map to create a new list by changing each country to be uppercase in the countries list
uppercased_countries = list(map(lambda country: country.upper(), countries))
print(uppercased_countries) 

#2. Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = list(map(lambda number: number ** 2, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#3. use map to change each name to uppercase in the names list
uppercased_names = list(map(lambda name: name.upper(), names))
print(uppercased_names)

#4. use filter to filter out countries containing 'land'.
# countries containing land
land_countries = list(filter(lambda country: 'land' in country, countries)) 
print(land_countries) 

# countries not containing land
no_land_countries = list(filter(lambda country: 'land' not in country, countries))
print(no_land_countries) 

#5. use filter to filter out countries having exactly six characters.
six_char_countries = list(filter(lambda country: len(country) == 6, countries))
print(six_char_countries) 

#6. Use filter to filter out countries containing six letters and more in the country list.
six_or_more_char_countries = list(filter(lambda country: len(country) >= 6, countries))
print(six_or_more_char_countries)

#7. use filter to filter out countries starting with 'E'
non_e_countries = list(filter(lambda country: not country.startswith('E'), countries))
print(non_e_countries)

#8. chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

# step by step: square -> filter even -> sum
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = map(lambda x: x ** 2, numbers)
evens = filter(lambda x: x % 2 == 0, squared)
total = reduce(lambda acc, x: acc + x, evens, 0)
print(total) # Output: 220 (sum of squared even numbers

#9. declare a function called get _string_lists which takes a list as a parameter then returns a list contraining only string items.
def get_string_lists(input_list): # function to get only string items from a list
    return list(filter(lambda item: isinstance(item, str), input_list)) # filtering only string items
# Example usage:
mixed_list = [1, 'hello', 3.14, 'world', True, 'Python'] #mixed list with different data types
string_list = get_string_lists(mixed_list) # list containing only string items
print(string_list)  # Output: ['hello', 'world', 'Python']

# 10. Use reduce to sum all the numbers in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = reduce(lambda acc, x: acc + x, numbers, 0)
print(total_sum) # output: 55

#11. Use reduce to concatenate all the countries to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
sentence = reduce(lambda acc, country: acc + ', ' + country, countries[:-1], '') + ', and ' + countries[-1] + ' are north European countries.'
print(sentence) # Output: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.

#12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
import countries as countries_data
def categorize_countries(pattern):
    return list(filter(lambda country: pattern in country.lower(), countries_data.countries))
# Example usage:
land_countries = categorize_countries('land')
print(land_countries)
ia_countries = categorize_countries('ia')
print(ia_countries)
island_countries = categorize_countries('island')
print(island_countries)
stan_countries = categorize_countries('stan')
print(stan_countries)
# Output: Countries containing the specified patterns

# 13. create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def country_starting_letters_count(countries_list):
    starting_letter_count = {}
    for country in countries_data.countries:
        first_letter = country[0].upper()
        if first_letter in starting_letter_count:
            starting_letter_count[first_letter] += 1
        else: 
            starting_letter_count[first_letter] = 1
    return starting_letter_count
# Example usage:
letter_count = country_starting_letters_count(countries_data.countries)
print(letter_count)

#14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries_data.py file
def get_first_ten_countries():
    return countries_data.countries[:10]
print(get_first_ten_countries())

#15. declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries_data.countries[-10:]
print(get_last_ten_countries())
