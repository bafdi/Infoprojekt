import pygame
import sys
from settings import *

def draw_grid(screen):
    screen.fill(BG_COLOR)

    for x in range(GRID_DIM):
        for y in range(GRID_DIM):

            #wo ist der punkt auf dem Bildschirm
            px = (x * CELL_SIZE) + MARGIN
            py = (y * CELL_SIZE) + MARGIN
            current_pos = (px, py)

            if x < GRID_DIM - 1:
                next_px = ((x + 1) * CELL_SIZE) + MARGIN
                next_py = py
                pygame.draw.line(screen, LINE_COLOR_SHADE, current_pos, (next_px, next_py), 10)

            #linie nach unten (nur wenn ich nciht am grid ende bin)
            if y < GRID_DIM - 1:
                next_px = px
                next_py = ((y + 1) * CELL_SIZE) + MARGIN
                pygame.draw.line(screen, LINE_COLOR_SHADE, current_pos,(next_px, next_py), 10)

            #linie nach rechts (nur wenn ich nicht am grid ende bin
            if x < GRID_DIM - 1:
                next_px = ((x + 1) * CELL_SIZE) + MARGIN
                next_py = py
                pygame.draw.line(screen, LINE_COLOR, current_pos, (next_px, next_py), 6)

            #linie nach unten (nur wenn ich nciht am grid ende bin)
            if y < GRID_DIM - 1:
                next_px = px
                next_py = ((y + 1) * CELL_SIZE) + MARGIN
                pygame.draw.line(screen, LINE_COLOR, current_pos,(next_px, next_py), 6)

