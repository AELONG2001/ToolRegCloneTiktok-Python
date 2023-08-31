import random
import string
from time import sleep


def random_number(min_num, max_num):
    return random.randint(min_num, max_num)


def wait(min_time, max_time):
    delay = random.uniform(min_time, max_time)
    sleep(delay)
