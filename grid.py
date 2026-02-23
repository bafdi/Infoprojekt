import pygame
from parameter import (BG_COLOR, BG_COLOR_TERMINAL, LINE_COLOR, LINE_COLOR_SHADE,
                       LINE_COLOR_TERMINAL, LINE_COLOR_TERMINAL_SHADE,
                       POINT_COLOR, BROKEN_COLOR, BROKEN_LINE_COLOR,
                       BROKEN_LINE_COLOR_SHADE, HOME_COLOR,
                       TELEPORTER_COLOR, point_radius)


def draw_grid(screen, broken_lines, params):
    grid_dim = params['grid_dim']
    cell_size = params['cell_size']
    margin = params['margin']
    screen.fill(BG_COLOR)

    for x in range(grid_dim):
        for y in range(grid_dim):
            px = (x * cell_size) + margin
            py = (y * cell_size) + margin
            current_pos = (px, py)

            p1 = (x, y)
            p2 = (x + 1, y)
            p3 = (x, y + 1)
            wall_r = sorted((p1, p2))
            wall_d = sorted((p1, p3))

            if x < grid_dim - 1:
                next_px = ((x + 1) * cell_size) + margin
                if wall_r not in broken_lines:
                    pygame.draw.line(screen, LINE_COLOR_SHADE, current_pos, (next_px, py), 10)
                    pygame.draw.line(screen, LINE_COLOR, current_pos, (next_px, py), 6)

            if y < grid_dim - 1:
                next_py = ((y + 1) * cell_size) + margin
                if wall_d not in broken_lines:
                    pygame.draw.line(screen, LINE_COLOR_SHADE, current_pos, (px, next_py), 10)
                    pygame.draw.line(screen, LINE_COLOR, current_pos, (px, next_py), 6)


def draw_broken_lines(screen, broken_lines, params):
    cell_size = params['cell_size']
    margin = params['margin']
    thickness = 12

    for start, end in broken_lines:
        x1, y1 = start
        x2, y2 = end

        px1 = (x1 * cell_size) + margin
        py1 = (y1 * cell_size) + margin
        px2 = (x2 * cell_size) + margin
        py2 = (y2 * cell_size) + margin

        if y1 == y2:
            pygame.draw.line(screen, BROKEN_COLOR, (px1 + 10, py1), (px2 - 10, py2), thickness)
            pygame.draw.line(screen, BROKEN_LINE_COLOR_SHADE, (px1 + 10, py1), (px2 - 10, py2), thickness // 3 + 1)
            pygame.draw.line(screen, BROKEN_LINE_COLOR, (px1 + 10, py1), (px2 - 10, py2), thickness // 4)

        if x1 == x2:
            pygame.draw.line(screen, BROKEN_COLOR, (px1, py1 + 10), (px2, py2 - 10), thickness)
            pygame.draw.line(screen, BROKEN_LINE_COLOR_SHADE, (px1, py1 + 10), (px2, py2 - 10), thickness // 3 + 1)
            pygame.draw.line(screen, BROKEN_LINE_COLOR, (px1, py1 + 10), (px2, py2 - 10), thickness // 4)


def draw_terminal_grid(screen, params):
    grid_dim = params['grid_dim']
    cell_size = params['cell_size']
    margin = params['margin']
    screen.fill(BG_COLOR_TERMINAL)

    for x in range(grid_dim):
        for y in range(grid_dim):
            px = (x * cell_size) + margin
            py = (y * cell_size) + margin
            current_pos = (px, py)

            if x < grid_dim - 1:
                next_px = ((x + 1) * cell_size) + margin
                pygame.draw.line(screen, LINE_COLOR_TERMINAL_SHADE, current_pos, (next_px, py), 10)

            if y < grid_dim - 1:
                next_py = ((y + 1) * cell_size) + margin
                pygame.draw.line(screen, LINE_COLOR_TERMINAL_SHADE, current_pos, (px, next_py), 10)

            if x < grid_dim - 1:
                next_px = ((x + 1) * cell_size) + margin
                pygame.draw.line(screen, LINE_COLOR_TERMINAL, current_pos, (next_px, py), 6)

            if y < grid_dim - 1:
                next_py = ((y + 1) * cell_size) + margin
                pygame.draw.line(screen, LINE_COLOR_TERMINAL, current_pos, (px, next_py), 6)


def draw_point(screen, point_locations, params):
    cell_size = params['cell_size']
    margin = params['margin']

    for point_location in point_locations:
        (x, y), (x2, y2) = point_location

        px = 0
        py = 0

        if x < x2:
            px = (x * cell_size) + margin + (cell_size // 2)
            py = (y * cell_size) + margin

        if y < y2:
            px = (x * cell_size) + margin
            py = (y * cell_size) + margin + (cell_size // 2)

        if px != 0 and py != 0:
            pygame.draw.circle(screen, POINT_COLOR, (px, py), point_radius)


def draw_teleporters(screen, teleporters, params):
    """Draw golden diamond markers on teleporter nodes."""
    cell_size = params['cell_size']
    margin = params['margin']
    size = max(6, cell_size // 8)

    for (x, y) in teleporters:
        cx = x * cell_size + margin
        cy = y * cell_size + margin
        diamond = [
            (cx, cy - size),
            (cx + size, cy),
            (cx, cy + size),
            (cx - size, cy),
        ]
        pygame.draw.polygon(screen, TELEPORTER_COLOR, diamond)
        pygame.draw.polygon(screen, (180, 140, 0), diamond, 2)


def draw_start_end(screen, params):
    grid_dim = params['grid_dim']
    cell_size = params['cell_size']
    margin = params['margin']

    start_x, start_y = margin, margin
    end_x = ((grid_dim - 1) * cell_size) + margin
    end_y = ((grid_dim - 1) * cell_size) + margin
    pygame.draw.circle(screen, HOME_COLOR, (start_x, start_y), 20, 2)
    pygame.draw.circle(screen, HOME_COLOR, (end_x, end_y), 20, 2)
