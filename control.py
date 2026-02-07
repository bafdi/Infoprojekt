import pygame
import sys
from parameter import *

def handle_input(player_pos, terminal_mode):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_RETURN:
                terminal_mode = not terminal_mode

            if event.key == pygame.K_w:
                if player_pos[0] > 0:
                    player_pos[0] -= 1

            if event.key == pygame.K_s:
                if player_pos[0] < grid_dim - 1:
                    player_pos[0] += 1

            if event.key == pygame.K_a:
                if player_pos[1] > 0:
                    player_pos[1] -= 1

            if event.key == pygame.K_d:
                if player_pos[1] < grid_dim - 1:
                    player_pos[1] += 1

    return player_pos, terminal_mode