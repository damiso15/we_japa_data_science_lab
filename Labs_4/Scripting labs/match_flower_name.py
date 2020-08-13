# For the following practice question you will need to write code in Python in the workspace below. 
# This will allow you to practice the concepts discussed in the Scripting lesson, such as reading 
# and writing files. You will see some older concepts too, but again, we have them there to review 
# and reinforce your understanding of those concepts.

# Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a 
# dictionary. The main (separate) function should take user input (user's first name and last name) 
# and parse the user input to identify the first letter of the first name. It should then use it 
# to print the flower name with the same first letter (from dictionary created in the first 
# function).

# Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower

# Write your code here

# HINT: create a dictionary from flowers.txt

def dictionary_flower():
    dict_list = {}

    with open('flowers.txt', 'r') as file:

        for lines in file.readlines():
            file_split = lines.rstrip('\n').split(': ')

            if len(file_split) > 1:
                dict_list[file_split[0]] = file_split[1]

    return dict_list


print(dictionary_flower())

# HINT: create a function


def user_input():
    name = input('Enter your First [space] Last name only: ')
    letter = name[0]
    dictionary = dictionary_flower()

    for key, value in dictionary.items():

        if key == letter:
            return value
    return


print(user_input())
