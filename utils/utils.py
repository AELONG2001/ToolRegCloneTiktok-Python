import random
import string
from time import sleep


def random_number(min_num, max_num):
    return random.randint(min_num, max_num)


def wait(min_time, max_time):
    delay = random.uniform(min_time, max_time)
    sleep(delay)

def generate_random_name(length=10):
    characters = string.ascii_letters + string.digits
    
    random_name = ''.join(random.choices(characters, k=length))
    
    return random_name
