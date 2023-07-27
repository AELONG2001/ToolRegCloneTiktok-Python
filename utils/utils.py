import random
import time


def random_number(min_num, max_num):
    return random.randint(min_num, max_num)


def wait(min_time, max_time):
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)
