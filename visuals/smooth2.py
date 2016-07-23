"""
LEDs start at random brightnesses and deltas (either up or down) and bounce
back when brightness goes out of its boundaries.
"""
from microbit import display
import random

[[display.set_pixel(x, y, 4) for y in range(5)] for x in range(4)]
delta = [[random.choice((-1, +1)) for _ in range(5)] for _ in range(5)]

while True:
    for x in range(5):
        for y in range(5):
            brightness = display.get_pixel(x, y)
            if ((brightness == 9 and delta[x][y] > 0)
                    or (brightness == 0 and delta[x][y] < 0)):
                delta[x][y] = -delta[x][y]
            if random.random() > .5:
                brightness += delta[x][y]
            display.set_pixel(x, y, brightness)
