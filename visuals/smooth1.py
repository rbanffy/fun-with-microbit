"""
LEDs start at random brightnesses and go up or down randomly by one level.
"""
import random

from microbit import display

while True:
    for x in range(5):
        for y in range(5):
            brightness = display.get_pixel(x, y)
            brightness += random.randrange(-1, 2)
            if brightness > 9:
                brightness = 9
            elif brightness < 0:
                brightness = 0
            display.set_pixel(x, y, brightness)
