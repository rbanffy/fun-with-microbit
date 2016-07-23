"""
Because cool computers have lots of blinking lights (or used to be).

Each LED gets a random brightness.
"""
import random

from microbit import display, sleep

while True:
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, random.randrange(0, 10))
    sleep(10)
