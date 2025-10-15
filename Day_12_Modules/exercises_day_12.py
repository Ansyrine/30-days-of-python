### Exercises

## exercises: level 1
#1 write a function which generates a six digit/character random_user_id
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print(random_user_id())

#2. modify the previous task. declare a function named user_id_gen_by_user. it doesn't take any parameters but it takes two inputs using input(). one of the unputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    characters = string.ascii_letters + string.digits
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_chars))
        user_ids.append(user_id)
    return user_ids
print(user_id_gen_by_user()) 

#3. write a function named rgb_colour_gen. it will generate rgb colors (3 values ranging from 0 to 255 each)
def rgb_colour_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
print(rgb_colour_gen())

## exercises: level 2
#1. write a function list_of_hexa_colours which returns any number of hexadecimal colours in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colours(num_colours):
    hexa_colours = []
    for _ in range(num_colours):
        colour = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hexa_colours.append(colour)
        return hexa_colours
print(list_of_hexa_colours(3))

#2. write a function list_of_rgb_colours which returns any number of rgb colours in an array.
def list_of_rgb_colours(num_colours):
    rgb_colours = []
    for _ in range(num_colours):
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colours.append(colour)
    return rgb_colours
print(list_of_rgb_colours(3))

#3. write a function generate_colours which can generate any number of hexa or rgb colours.
def generate_colours(colour_type, num_colours):
    if colour_type == 'hexa':
        return list_of_hexa_colours(num_colours)
    elif colour_type == 'rgb':
        return list_of_rgb_colours(num_colours)
    elif colour_type == 'both':
        return list_of_hexa_colours(num_colours), list_of_rgb_colours(num_colours)
    else: 
        return "Invalid colour type. Please choose 'hexa', 'rgb', or 'both'."
print(generate_colours('hexa', 3))
print(generate_colours('hexa', 1))
print(generate_colours('rgb', 3))
print(generate_colours('rgb', 1))
print(generate_colours('both', 3))
print(generate_colours('both', 1))


## exercises: level 3
#1. call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(input_list):
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list
print(shuffle_list([1, 2, 3, 4, 5]))

#2. write a function which returns an array of seven random numbers in a range of 0-9. all numbers must be unique.
def unique_random_numbers():
    return random.sample(range(10), 7)
print(unique_random_numbers())
