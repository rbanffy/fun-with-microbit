"""
Here only for making testing easier - libraries on the Micro Bit are a pain.
"""


def xy(channel):
    """
    Returns x,y display coordinates for a channel

    >>> xy(0)
    (0, 0)
    >>> xy(3)
    (0, 0)
    >>> xy(4)
    (0, 1)
    >>> xy(7)
    (0, 1)
    >>> xy(21)
    (1, 0)
    >>> xy(42)
    (2, 0)

    """
    x = channel // 20
    y = channel // 4 % 5
    return x, y
