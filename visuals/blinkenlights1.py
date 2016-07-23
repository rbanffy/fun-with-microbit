"""
Because cool computers have lots of blinking lights (or used to be).

Each LED gets a random brightness.
"""
from microbit import display, sleep
import random

while True:
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, random.randrange(0, 10))
    sleep(10)
