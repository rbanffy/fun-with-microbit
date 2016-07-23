"""
Scans channels from 0 to 99 for data traffic. Monitors actual number of
messages received, not channel signals. Button A cycles through available data
rates.
"""
from microbit import button_a, display, sleep
import radio


def cycle(iterable):  # I know. MicroPython doesn't have itertools
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element

radio.on()

DATA_RATES = cycle((radio.RATE_1MBIT, radio.RATE_2MBIT, radio.RATE_250KBIT))
data_rate = DATA_RATES.__next__()

while True:
    for x in range(5):
        for y in range(5):
            brightness = 0
            display.set_pixel(x, y, 2)
            for offset in range(4):
                channel = 20 * x + 4 * y + offset
                radio.config(channel=channel)
                sleep(50)  # Wait .05 seconds for anything
                while radio.receive_bytes() is not None:
                    brightness += 3  # Increment for every message received.
                if button_a.was_pressed():
                    data_rate = DATA_RATES.__next__()
                    radio.config(data_rate=data_rate)
            if brightness > 9:
                brightness = 9
            display.set_pixel(x, y, brightness)

radio.off()
