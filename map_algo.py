import random
from parameter import *

def generate_direction():
    direction = random.randint(0, 1)
    return direction

def generate_broken_lines(qty=None):
    if qty is None:
        qty = broken_lines_qty
    broken_lines = []

    while len(broken_lines) < qty:
        direction = generate_direction()
        x = random.randint(0, grid_dim - 1)
        y = random.randint(0, grid_dim - 1)

        if direction == 0:
            next_x = x + 1
            next_y = y
        else:
            next_x = x
            next_y = y + 1

        if next_x >= grid_dim or next_y >= grid_dim:
            continue


        p1 = (x, y)
        p2 = (next_x, next_y)
        wall = tuple(sorted((p1, p2)))

        if wall not in broken_lines:
            broken_lines.append(wall)

    return broken_lines


def generate_points(broken_lines, qty=None):
    if qty is None:
        qty = point_qty
    point_locations = []

    while len(point_locations) < qty:
        x = random.randint(0, grid_dim - 1)
        y = random.randint(0 , grid_dim - 1)
        direction = random.randint(0, 1) # 0 - diagonal ;1 - horizontal

        if direction == 0:
            next_x = x + 1
            next_y = y

        else:
            next_x = x
            next_y = y + 1

        if next_x >= grid_dim or next_y >= grid_dim:
            continue

        point_location = tuple(sorted(((x, y),(next_x, next_y))))

        if point_location not in broken_lines and point_location not in point_locations:
            point_locations.append(point_location)

    return point_locations
