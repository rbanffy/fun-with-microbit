from microbit import button_a, button_b, display, sleep

delay = 20


def fade():
    for x in range(5):
        for y in range(5):
            brightness = display.get_pixel(x, y)
            if brightness > 0:
                display.set_pixel(x, y, brightness - 1)

while True:
    for x in range(5):
        for y in range(5):
            fade()
            if button_a.is_pressed():
                delay += 1
            elif delay > 0 and button_b.is_pressed():
                delay -= 1
            display.set_pixel(x, y, 9)
            for _ in range(delay):
                sleep(1)
