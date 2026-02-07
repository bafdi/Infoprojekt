import pygame
import sys
from parameter import *

def draw_grid(screen, broken_lines, direction):
    screen.fill(BG_COLOR)

    for x in range(grid_dim):
        for y in range(grid_dim):

            #wo ist der punkt auf dem Bildschirm
            px = (x * cell_size) + margin
            py = (y * cell_size) + margin
            current_pos = (px, py)

            #linie nach rechts (nur wenn ich nicht am grid ende bin)
            if x < grid_dim - 1:
                next_px = ((x + 1) * cell_size) + margin
                next_py = py
                pygame.draw.line(screen, LINE_COLOR_SHADE, current_pos, (next_px, next_py), 10)
                pygame.draw.line(screen, LINE_COLOR, current_pos, (next_px, next_py), 6)

            #linie nach unten (nur wenn ich nciht am grid ende bin)
            if y < grid_dim - 1:
                next_px = px
                next_py = ((y + 1) * cell_size) + margin
                pygame.draw.line(screen, LINE_COLOR_SHADE, current_pos, (next_px, next_py), 10)
                pygame.draw.line(screen, LINE_COLOR, current_pos,(next_px, next_py), 6)

def draw_broken_lines(screen, broken_lines, direction):
    thickness = 12

    for line in broken_lines:
        x, y, next_x, next_y = line
        px = (x * cell_size) + margin
        py = (y * cell_size) + margin

        if next_x > x:
            next_px = (next_x * cell_size) + margin
            next_py = py
            pygame.draw.line(screen, BROKEN_COLOR, (px + 10, py), (next_px - 10, next_py), thickness)
            pygame.draw.line(screen, BROKEN_LINE_COLOR_SHADE, (px + 10, py), (next_px - 10, next_py), thickness//3 + 1)
            pygame.draw.line(screen, BROKEN_LINE_COLOR, (px + 10, py), (next_px - 10, next_py), thickness//4)

        if next_y > y:
            next_px = px
            next_py = ((y + 1) * cell_size) + margin
            pygame.draw.line(screen, BROKEN_COLOR, (px, py + 10), (next_px, next_py - 10), thickness)
            pygame.draw.line(screen, BROKEN_LINE_COLOR_SHADE, (px, py + 10), (next_px, next_py - 10), thickness //3 + 1)
            pygame.draw.line(screen, BROKEN_LINE_COLOR, (px, py + 10), (next_px, next_py - 10), thickness//4)


def draw_terminal_grid(screen):
    screen.fill(BG_COLOR_TERMINAL)

    for x in range(grid_dim):
        for y in range(grid_dim):
            # wo ist der punkt auf dem Bildschirm
            px = (x * cell_size) + margin
            py = (y * cell_size) + margin
            current_pos = (px, py)

            if x < grid_dim - 1:
                next_px = ((x + 1) * cell_size) + margin
                next_py = py
                pygame.draw.line(screen, LINE_COLOR_TERMINAL_SHADE, current_pos, (next_px, next_py), 10)

            # linie nach unten (nur wenn ich nciht am grid ende bin)
            if y < grid_dim - 1:
                next_px = px
                next_py = ((y + 1) * cell_size) + margin
                pygame.draw.line(screen, LINE_COLOR_TERMINAL_SHADE, current_pos, (next_px, next_py), 10)

            # linie nach rechts (nur wenn ich nicht am grid ende bin
            if x < grid_dim - 1:
                next_px = ((x + 1) * cell_size) + margin
                next_py = py
                pygame.draw.line(screen, LINE_COLOR_TERMINAL, current_pos, (next_px, next_py), 6)

            # linie nach unten (nur wenn ich nciht am grid ende bin)
            if y < grid_dim - 1:
                next_px = px
                next_py = ((y + 1) * cell_size) + margin
                pygame.draw.line(screen, LINE_COLOR_TERMINAL, current_pos, (next_px, next_py), 6)