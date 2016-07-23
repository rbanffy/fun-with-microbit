"""
Because cool computers have lots of blinking lights (or used to be).

Each LED is either on or off.
"""
import random

from microbit import display, sleep

while True:
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, random.choice([0, 9]))
    sleep(100)
