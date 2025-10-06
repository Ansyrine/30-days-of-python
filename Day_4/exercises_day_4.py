# exercise 1
thirty = 'Thirty' 
days = 'Days'
of = 'Of'
python = 'Python'

sentence = thirty + ' ' + days + ' ' + of + ' ' + python
print(sentence)

# exercise 2
coding = 'Coding'
fo_r = 'for'
all = 'all'

sentence_one = coding + ' ' + fo_r + ' ' + all 
print(sentence_one) 

# exercise 3
company = sentence_one

# exercise 4
print(sentence_one)

# exercise 5
print(len(company)) 

# exercise 6 
print(company.upper()) 

# exercise 7
aiming = 'THIS NEEDS TO BE LOWER CASE'
print(aiming.lower())

# exercise 8
coding_str = 'Coding For All'
print(coding_str.capitalize()) 
print(coding_str.title())  
print(coding_str.swapcase()) 

# exercise 9 

print(coding_str.strip(coding))

#exercise 10
print(coding_str.startswith(coding))

# exercise 11
print(coding_str.replace(coding, python))

# exercise 12
python_str = 'Python for everyone'
print(python_str)
everyone = 'everyone'
print(python_str.replace(everyone, all)) 

# exercise 13
split_result = coding_str.split(' ')
print(split_result)

# exercise 14
tech_companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
split_companies = tech_companies.split(', ')
print(split_companies)

# exercise 15
first_letter = coding_str[0]
print(first_letter)

# exercise 16 
print(len(coding_str)-1)

# exercise 17
print(coding_str[9]) 

# exercise 18
name = 'Python For Everyone'
acronym = ''.join(word[0] for word in name.split())
print(acronym)

# exercise 19
name_one = 'Coding For All'
acronym_one = ''.join(word[0] for word in name_one.split())
print(acronym_one)

# exercise 20
print(coding_str.index('C'))

# exercise 21
print(coding_str.index('F'))

# exercise 22
coding_str_two = 'coding for all people'
print(coding_str_two.rfind('l'))

# exercise 23
sentence_two = 'you cannot end a sentence with because because because is a conjunction'
print(sentence_two.index('because'))

# exercise 24
print(sentence_two.rindex('because'))

# exercise 25
print(sentence_two.replace('because', ''))

# exercise 26
print(sentence_two.find('because'))

# exercise 27
print(sentence_two.replace('because', ''))

# exercise 28
print(coding_str.startswith('Coding'))

# exercise 29 
print(coding_str.endswith('coding'))

# exercise 30
long_coding_str = '   Coding For All    '
print(long_coding_str)
print(long_coding_str.strip( ))

# exercise 31 
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# exercise 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'falcon']
joined = ' # '.join(libraries)
print(joined)

# exercise 33
print('I am enjoying this challenge. \nI just wonder what is next.')

# exercise 34
print('Name\tAge\tCountry\tCity')
print('Sylas\t22\tEngland\tClitheroe')

# exercise 35
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, int(area)))

# exercise 36
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")