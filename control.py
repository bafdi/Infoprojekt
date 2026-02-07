import pygame
import sys
from parameter import *

def can_move(current_pos, target_pos, broken_lines, grid_dim):
    if target_pos[0] < 0 or target_pos[0] >= grid_dim:
        return False
    if target_pos[1] < 0 or target_pos[1] >= grid_dim:
        return False

    p1 = (current_pos[0], current_pos[1])
    p2 = (target_pos[0], target_pos[1])

    move = tuple(sorted((p1, p2)))

    if move in broken_lines:
        return False
    return True


def handle_input(player_pos, terminal_mode, broken_lines):
    next_pos = list(player_pos)
    moves = False

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

            if terminal_mode == False:
                if event.key == pygame.K_w:
                    next_pos[1] -= 1
                    moves = True

                if event.key == pygame.K_s:
                    next_pos[1] += 1
                    moves = True

                if event.key == pygame.K_a:
                    next_pos[0] -= 1
                    moves = True

                if event.key == pygame.K_d:
                    next_pos[0] += 1
                    moves = True

                if moves:
                    if can_move(player_pos, next_pos, broken_lines, grid_dim):
                        player_pos = next_pos

            else:
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