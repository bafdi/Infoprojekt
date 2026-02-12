import pygame
from parameter import *

def draw_player(screen, grid_x, grid_y):
    px = margin + (grid_x * cell_size)
    py = margin + (grid_y * cell_size)

    rect = pygame.Rect((px-player_size//2), (py-player_size//2), player_size, player_size)
    pygame.draw.rect(screen, PLAYER_COLOR, rect)

def draw_terminal_line(screen, player_path, color):
    for i in range(len(player_path) - 1):
        start = player_path[i]
        end = player_path[i + 1]

        start_px = (start[0] * cell_size) + margin
        start_py = (start[1] * cell_size) + margin
        end_px = (end[0] * cell_size) + margin
        end_py = (end[1] * cell_size) + margin

        pygame.draw.line(screen, color, (start_px, start_py), (end_px, end_py), 6)
        pygame.draw.circle(screen, color, (start_px + 1, start_py + 1), 3)