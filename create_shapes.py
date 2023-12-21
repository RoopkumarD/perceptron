import math
import random
from typing import Tuple


def coordinate_dist(p1: Tuple[int, int], p2: Tuple[int, int]):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def create_random_rectangle(height: int, width: int):
    row0 = random.randrange(0, height - 1)
    row1 = random.randrange(row0 + 1, height)

    col0 = random.randrange(0, width - 1)
    col1 = random.randrange(col0 + 1, width)

    return [(i, j) for i in range(row0, row1 + 1) for j in range(col0, col1 + 1)]
    # I did this because only those points have value 1 and those affect weights or change dot product
    # value as 0 * something = 0

    # initial = [[0.0] * width for _ in range(height)]
    # for i in range(row0, row1 + 1):
    #     for j in range(col0, col1 + 1):
    #         initial[i][j] = 1.0
    #
    # return initial


def create_random_circle(height: int, width: int):
    # assuming the frame is square
    if height != width:
        raise Exception("Need a square frame")

    radius = random.randint(1, math.floor((width - 1) / 2))
    center = (
        random.randint(radius, height - radius - 1),
        random.randint(radius, width - radius - 1),
    )

    return [
        (i, j)
        for i in range(height)
        for j in range(width)
        if coordinate_dist((i, j), center) <= radius
    ]
    # I did this because only those points have value 1 and those affect weights or change dot product
    # value as 0 * something = 0

    # initial = [
    #     [
    #         1.0 if coordinate_dist((i, j), center) <= radius else 0.0
    #         for j in range(width)
    #     ]
    #     for i in range(height)
    # ]
    #
    # return initial
