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


def handle_input(player_pos, terminal_mode, broken_lines, player_path, menu_mode):
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
                moved_in_terminal = False

                if event.key == pygame.K_w:
                    if player_pos[1] > 0:
                        player_pos[1] -= 1
                        moved_in_terminal = True

                if event.key == pygame.K_s:
                    if player_pos[1] < grid_dim - 1:
                        player_pos[1] += 1
                        moved_in_terminal = True

                if event.key == pygame.K_a:
                    if player_pos[0] > 0:
                        player_pos[0] -= 1
                        moved_in_terminal = True

                if event.key == pygame.K_d:
                    if player_pos[0] < grid_dim - 1:
                        player_pos[0] += 1
                        moved_in_terminal = True

                if moved_in_terminal:
                    current = tuple(player_pos)
                    if len(player_path) > 1 and current == player_path[-2]:
                        player_path.pop()
                    else:
                        player_path.append(current)

                    end_pos = (grid_dim-1, grid_dim-1)
                    if current == end_pos:
                        check = True

    return player_pos, terminal_mode, check, menu_mode

def check_win(player_pos, player_path, broken_lines, point_locations):
    start = (0, 0)
    end = (grid_dim-1, grid_dim-1)

    if player_path[0] != start or player_path[-1] != end:
        return False

    path_lines = []

    for i in range(0, len(player_path)-1):
        pos_1 = player_path[i]
        pos_2 = player_path[i + 1]
        path_line = tuple(sorted((pos_1, pos_2)))
        path_lines.append(path_line)

        if path_line in broken_lines:
            return False

    for point in point_locations:
        if point not in path_lines:
            return False

    return True

def start_new_game():
    player_pos = [0, 0]
    player_path = [(0, 0)]
    broken_lines = map_algo.generate_broken_lines()
    points = map_algo.generate_points(broken_lines)
    return player_pos, player_path, broken_lines, points

def draw_won(screen, player_path):
    screen.fill(WIN_BG_COLOR)
    player.draw_terminal_line(screen, player_path, color=(0, 140, 0))
    pygame.display.flip()
    pygame.time.wait(3500)


def draw_lost(screen, player_path):
    screen.fill(LOSE_BG_COLOR)
    player.draw_terminal_line(screen, player_path, color=(140, 0, 0))
    pygame.display.flip()
    pygame.time.wait(2000)

