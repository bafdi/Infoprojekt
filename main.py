import pygame
import grid
import player
import control
import map_algo
import ui
from parameter import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("THE GRID")
    screen.fill(BG_COLOR)
    clock = pygame.time.Clock()

    player_pos = [0, 0]
    player_path = [(0, 0)]

    broken_lines = map_algo.generate_broken_lines()
    points = map_algo.generate_points(broken_lines)
    print(broken_lines)
    print(cell_size)
    print(points)

    terminal_mode = False

    while True:
        player_pos, terminal_mode, check = control.handle_input(player_pos, terminal_mode, broken_lines, player_path)

        if check:
            has_won = control.check_win(player_pos, player_path, broken_lines, points)

            if has_won:
                control.draw_won(screen, player_path)
                terminal_mode = False
                player_pos, player_path, broken_lines, points = control.start_new_game()

            else:
                control.draw_lost(screen, player_path)
                terminal_mode = False
                player_pos = [0, 0]
                player_path = [(0, 0)]

        if terminal_mode:
            grid.draw_terminal_grid(screen)
            player.draw_terminal_line(screen, player_path, PLAYER_COLOR)
            print(player_path)


        else:
            player_path.clear()
            player_path.append(tuple(player_pos))
            grid.draw_grid(screen, broken_lines)
            grid.draw_broken_lines(screen, broken_lines)
            grid.draw_point(screen, points)

        player.draw_player(screen, player_pos[0], player_pos[1])
        grid.draw_start_end(screen)
        ui.draw_hud(screen, terminal_mode)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
