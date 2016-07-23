"""
Transmit a message to random channels continuously.
"""
import random

import radio
from microbit import display


def xy(channel):
    x = channel // 20
    y = channel // 4 % 5
    return x, y

radio.on()

while True:
    channel = random.randrange(100)
    radio.config(channel=channel)
    x, y = xy(channel)
    display.set_pixel(x, y, 9)
    radio.send('hello, microbit')
    display.set_pixel(x, y, 0)

radio.off()
