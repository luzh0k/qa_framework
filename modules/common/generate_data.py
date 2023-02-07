import random
def generate_string(n, k):
    finish_string = ''
    origin = 'qwertyuiopasddffghjklmnbvcxz'
    for i in range(k):
        for j in range(n):
            finish_string += origin[int(random.uniform(0, len(origin)))]
        finish_string += " "
    return finish_string

def generate_number(n):
    number = random.uniform(0, n)
    return int(number)


print(generate_number(33))