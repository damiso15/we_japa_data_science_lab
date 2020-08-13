# Write a function called generate_password that selects three random words from the list of words 
# word_list and concatenates them into a single string. Your function should not accept any 
# arguments and should reference the global variable word_list to build the password.

# Use an import statement at the top

import secrets

# Write your code here
word_file = "words.txt"
word_list = []

# fill up the word_list
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)


# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces


def generate_password():
    # length = len(word_list)
    # for element in range(length):
    password1 = secrets.choice(word_list)
    while True:
        password2 = secrets.choice(word_list)
        if password1 == password2:
            pass
        else:
            break

    while True:
        password3 = secrets.choice(word_list)
        if password1 == password3:
            pass
        elif password2 == password3:
            pass
        else:
            break

    return password1 + password2 + password3


# test your function

print(generate_password())
