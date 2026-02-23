import random
from parameter import point_qty
from entity import Enemy


def generate_direction():
    direction = random.randint(0, 1)
    return direction


def generate_broken_lines(params):
    grid_dim = params['grid_dim']
    broken_lines_qty = params['broken_lines_qty']
    broken_lines = []

    while len(broken_lines) < broken_lines_qty:
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


def generate_points(broken_lines, params):
    grid_dim = params['grid_dim']
    point_locations = []

    while len(point_locations) < point_qty:
        x = random.randint(0, grid_dim - 1)
        y = random.randint(0, grid_dim - 1)
        direction = random.randint(0, 1)

        if direction == 0:
            next_x = x + 1
            next_y = y
        else:
            next_x = x
            next_y = y + 1

        if next_x >= grid_dim or next_y >= grid_dim:
            continue

        point_location = tuple(sorted(((x, y), (next_x, next_y))))

        if point_location not in broken_lines and point_location not in point_locations:
            point_locations.append(point_location)

    return point_locations


def generate_enemies(params, broken_lines):
    """Generate patrolling enemies; count scales with level (0 on level 1)."""
    grid_dim = params['grid_dim']
    level_num = grid_dim - 4          # level 1 → grid_dim 5
    num_enemies = min(max(0, level_num - 1), 4)

    forbidden = {(0, 0), (grid_dim - 1, grid_dim - 1)}
    used_positions = set(forbidden)
    enemies = []
    attempts = 0

    while len(enemies) < num_enemies and attempts < 200:
        attempts += 1
        x = random.randint(0, grid_dim - 1)
        y = random.randint(0, grid_dim - 1)
        if (x, y) in used_positions:
            continue
        axis = random.choice(['h', 'v'])
        direction = random.choice([1, -1])
        enemies.append(Enemy(x, y, axis, direction))
        used_positions.add((x, y))

    return enemies


def generate_teleporters(params, broken_lines):
    """Return a dict mapping each teleporter node to its partner node."""
    grid_dim = params['grid_dim']
    forbidden = {(0, 0), (grid_dim - 1, grid_dim - 1)}
    all_nodes = [(x, y) for x in range(grid_dim) for y in range(grid_dim)]
    valid = [n for n in all_nodes if n not in forbidden]

    num_pairs = max(1, grid_dim // 4)
    teleporters = {}
    used = set()
    attempts = 0
    pairs_created = 0

    while pairs_created < num_pairs and attempts < 200:
        attempts += 1
        available = [n for n in valid if n not in used]
        if len(available) < 2:
            break
        a = random.choice(available)
        available.remove(a)
        b = random.choice(available)
        teleporters[a] = b
        teleporters[b] = a
        used.add(a)
        used.add(b)
        pairs_created += 1

    return teleporters
