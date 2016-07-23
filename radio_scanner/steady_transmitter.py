"""
Transmits continuously a message on a randomly selected channel. Buttons A/B
change channel up/down. When shaken, picks one randomly.

Used in conjunction with scanner.py.
"""
from microbit import display, accelerometer, button_a, button_b
import radio
import random


def new_channel():
    return random.randrange(100)


def xy(channel):
    x = channel // 20
    y = channel // 4 % 5
    return x, y

radio.on()

channel = new_channel()
x, y = xy(channel)
radio.config(channel=channel)

while True:
    display.set_pixel(x, y, 4)
    radio.send('hello, microbit')
    display.set_pixel(x, y, 0)
    if accelerometer.is_gesture('shake'):
        channel = new_channel()
        radio.config(channel=channel)
        x, y = xy(channel)
    if button_a.was_pressed():
        channel += 1
        radio.config(channel=channel)
        if channel > 99:
            channel = 0
        x, y = xy(channel)
    if button_b.was_pressed():
        channel -= 1
        radio.config(channel=channel)
        if channel == 0:
            channel = 99
        x, y = xy(channel)

radio.off()
