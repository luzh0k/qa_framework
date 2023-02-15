import requests
import json
from dotenv import load_dotenv
import os
import random
def generate_number(x,y):
    number = max(x,y)
    os.environ['my_number'] = str(number)
    return number

def plus_annumber(x):
    number = int(os.getenv("my_number"))
    return number+x

print(generate_number(29, 66))
print(plus_annumber(4))