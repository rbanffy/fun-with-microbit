"""
Waves originating from 1,1
"""
from microbit import display, sleep
from math import sin, sqrt

offset = 0
while True:
    for x in range(5):
        for y in range(5):
            brightness = int(
                4.5 + 4.5 * sin(sqrt((x - 1) ** 2 + (y - 1) ** 2) * 1.4 - offset))
            display.set_pixel(x, y, brightness)
    offset += 1
    sleep(20)
