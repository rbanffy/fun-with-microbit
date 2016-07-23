from microbit import button_a, button_b, display, sleep

# I need to keep my own brightess values
brightness = [[0 for _ in range(5)] for _ in range(5)]

delay = 20


def fade(brightness):
    for x in range(5):
        for y in range(5):
            if brightness[x][y] > 0:
                brightness[x][y] -= .5
            elif brightness[x][y] < 0:
                brightness[x][y] = 0
            display.set_pixel(x, y, int(brightness[x][y]))

while True:
    for x in range(5):
        for y in range(5):
            fade(brightness)
            if button_a.is_pressed():
                delay += 1
            elif delay > 0 and button_b.is_pressed():
                delay -= 1
            brightness[x][y] = 9
            display.set_pixel(x, y, 9)
            for _ in range(delay):
                sleep(1)
