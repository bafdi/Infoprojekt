import pygame
from parameter import *

player_size = 20

def draw_player(screen, grid_x, grid_y):
    py = MARGIN + (grid_x * CELL_SIZE)
    px = MARGIN + (grid_y * CELL_SIZE)

    rect = pygame.Rect((px-player_size/2), (py-player_size/2), player_size, player_size)
    pygame.draw.rect(screen, PLAYER_COLOR, rect)