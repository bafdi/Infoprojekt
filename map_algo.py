import random
from parameter import *

def generate_direction():
    direction = random.randint(0, 1)
    return direction

def generate_broken_lines():
    broken_lines = []

    while len(broken_lines) < broken_lines_qty:
        direction = generate_direction()
        x = random.randint(0, grid_dim - 1)
        y = random.randint(0, grid_dim - 1)

        if direction == 0:
            next_x = x + 1
            next_y = y
            if next_x >= grid_dim:
                next_x = x
        else:
            next_x = x
            next_y = y + 1
            if next_y >= grid_dim:
                next_y = y

        position = (x, y, next_x, next_y)
        broken_lines.append(position)

    return broken_lines, direction

