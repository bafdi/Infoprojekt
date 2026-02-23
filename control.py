import pygame
import sys
import player
import map_algo
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


def handle_input(player_pos, terminal_mode, broken_lines, player_path, menu_mode,
                 params, teleporters, remaining_moves):
    grid_dim = params['grid_dim']
    max_moves = params['max_moves']
    next_pos = list(player_pos)
    moves = False
    check = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_mode = not menu_mode

            if event.key == pygame.K_RETURN:
                terminal_mode = not terminal_mode
                if terminal_mode:
                    player_path.clear()
                    player_path.append(tuple(player_pos))
                    remaining_moves = max_moves

            if terminal_mode == False:
                if event.key == pygame.K_UP:
                    next_pos[1] -= 1
                    moves = True

                if event.key == pygame.K_DOWN:
                    next_pos[1] += 1
                    moves = True

                if event.key == pygame.K_LEFT:
                    next_pos[0] -= 1
                    moves = True

                if event.key == pygame.K_RIGHT:
                    next_pos[0] += 1
                    moves = True

                if moves:
                    if can_move(player_pos, next_pos, broken_lines, grid_dim):
                        player_pos = next_pos
                        # Teleporter check (normal mode)
                        t_key = tuple(player_pos)
                        if t_key in teleporters:
                            dest = teleporters[t_key]
                            player_pos = list(dest)

            else:
                # --- Terminal mode ---
                # Backspace: undo last step
                if event.key == pygame.K_BACKSPACE and len(player_path) > 1:
                    player_path.pop()
                    player_pos = list(player_path[-1])
                    remaining_moves = min(remaining_moves + 1, max_moves)
                    continue

                moved_in_terminal = False
                old_pos = list(player_pos)

                # Only allow new moves when below the limit
                if remaining_moves > 0:
                    if event.key == pygame.K_UP:
                        if player_pos[1] > 0:
                            player_pos[1] -= 1
                            moved_in_terminal = True

                    if event.key == pygame.K_DOWN:
                        if player_pos[1] < grid_dim - 1:
                            player_pos[1] += 1
                            moved_in_terminal = True

                    if event.key == pygame.K_LEFT:
                        if player_pos[0] > 0:
                            player_pos[0] -= 1
                            moved_in_terminal = True

                    if event.key == pygame.K_RIGHT:
                        if player_pos[0] < grid_dim - 1:
                            player_pos[0] += 1
                            moved_in_terminal = True

                if moved_in_terminal:
                    current = tuple(player_pos)
                    # Teleporter check (terminal mode)
                    if current in teleporters:
                        dest = teleporters[current]
                        player_pos = list(dest)
                        current = tuple(player_pos)

                    if len(player_path) > 1 and current == player_path[-2]:
                        player_path.pop()
                        remaining_moves += 1
                    elif current in player_path:
                        player_pos = old_pos
                    else:
                        player_path.append(current)
                        remaining_moves -= 1

                    end_pos = (grid_dim - 1, grid_dim - 1)
                    if current == end_pos:
                        check = True

    return player_pos, terminal_mode, check, menu_mode, remaining_moves


def check_win(player_pos, player_path, broken_lines, params):
    grid_dim = params['grid_dim']
    start = (0, 0)
    end = (grid_dim - 1, grid_dim - 1)

    if player_path[0] != start or player_path[-1] != end:
        return False

    for i in range(0, len(player_path) - 1):
        pos_1 = player_path[i]
        pos_2 = player_path[i + 1]
        path_line = tuple(sorted((pos_1, pos_2)))

        if path_line in broken_lines:
            return False

    return True


def start_new_game(params):
    player_pos = [0, 0]
    player_path = [(0, 0)]
    broken_lines = map_algo.generate_broken_lines(params)
    points = map_algo.generate_points(broken_lines, params)
    return player_pos, player_path, broken_lines, points
