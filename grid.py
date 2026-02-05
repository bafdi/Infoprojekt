import pygame
import sys
from parameter import *

def draw_grid(screen):
    screen.fill(BG_COLOR)

    for x in range(grid_dim):
        for y in range(grid_dim):

            #wo ist der punkt auf dem Bildschirm
            px = (x * cell_size) + margin
            py = (y * cell_size) + margin
            current_pos = (px, py)

            if x < grid_dim - 1:
                next_px = ((x + 1) * cell_size) + margin
                next_py = py
                pygame.draw.line(screen, LINE_COLOR_SHADE, current_pos, (next_px, next_py), 10)

            #linie nach unten (nur wenn ich nciht am grid ende bin)
            if y < grid_dim - 1:
                next_px = px
                next_py = ((y + 1) * cell_size) + margin
                pygame.draw.line(screen, LINE_COLOR_SHADE, current_pos,(next_px, next_py), 10)

            #linie nach rechts (nur wenn ich nicht am grid ende bin
            if x < grid_dim - 1:
                next_px = ((x + 1) * cell_size) + margin
                next_py = py
                pygame.draw.line(screen, LINE_COLOR, current_pos, (next_px, next_py), 6)

            #linie nach unten (nur wenn ich nciht am grid ende bin)
            if y < grid_dim - 1:
                next_px = px
                next_py = ((y + 1) * cell_size) + margin
                pygame.draw.line(screen, LINE_COLOR, current_pos,(next_px, next_py), 6)


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