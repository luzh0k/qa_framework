import random

# function for generating random string with k words, each of them with n symbols
def generate_string(n, k):
    finish_string = ''
    origin = 'qwertyuiopasddffghjklmnbvcxz'
    for i in range(k):
        for j in range(n):
            finish_string += origin[int(random.uniform(0, len(origin)))]
        finish_string += " "
    return finish_string

# function for generating random integer number in range (0, n) for numeric test-data

def generate_number(n):
    number = random.uniform(0, n)
    return int(number)