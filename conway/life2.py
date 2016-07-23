"""
Game of life
"""
import random
from microbit import display, sleep

present = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
future = [[0 for _ in range(5)] for _ in range(5)]


def count_living_neighbors(x, y, world):
    """Returns the count of living neighbors"""
    x_right = x + 1
    if x_right > 4:
        x_right = 0
    y_down = y + 1
    if y_down > 4:
        y_down = 0

    return sum([
        world[x-1][y-1], world[x][y-1], world[x_right][y-1],
        world[x-1][y], world[x_right][y],
        world[x-1][y_down], world[x][y_down], world[x_right][y_down],
    ])

def evolve(present):
    future = [[0 for _ in range(5)] for _ in range(5)]
    for x in range(5):
        for y in range(5):
            living_neighbors = count_living_neighbors(x, y, present)
            if living_neighbors < 2:  # Die of solitude
                future[x][y] = 0
            elif living_neighbors == 2:  # Stay as-is
                future[x][y] = present[x][y]
            elif living_neighbors == 3:  # Be born
                future[x][y] = 1
            else:  # Starve to death
                future[x][y] = 0
    return future

def show(present):
    for x in range(5):
        for y in range(5):
            if present[x][y] == 1:
                display.set_pixel(x, y, 9)
                
def fade(how_much=1):
    for x in range(5):
        for y in range(5):
            brightness = display.get_pixel(x, y)
            if brightness >= how_much:
                display.set_pixel(x, y, brightness - how_much)


while True:
    future = evolve(present)
    if present == future:
        # We are at a boring state and should restart
        future = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
    show(future)
    present = future
    fade()
    sleep(100)
    fade()
    sleep(100)
