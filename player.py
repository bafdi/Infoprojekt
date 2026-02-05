import pygame
from parameter import *

def draw_player(screen, grid_x, grid_y):
    py = margin + (grid_x * cell_size)
    px = margin + (grid_y * cell_size)

    rect = pygame.Rect((px-player_size/2), (py-player_size/2), player_size, player_size)
    pygame.draw.rect(screen, PLAYER_COLOR, rect)