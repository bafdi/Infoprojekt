import pygame
import sys
import grid
import player
import control
import map_algo
from parameter import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("PyGame")
    screen.fill(BG_COLOR)
    clock = pygame.time.Clock()
    player_pos = [0, 2]
    broken_lines = map_algo.generate_broken_lines()
    print(broken_lines)
    print(cell_size)
    points = map_algo.generate_points(broken_lines)
    print(points)
    terminal_mode = False

    while True:
        player_pos, terminal_mode = control.handle_input(player_pos, terminal_mode, broken_lines)
        if terminal_mode:
            grid.draw_terminal_grid(screen)
        else:
            grid.draw_grid(screen, broken_lines)
            grid.draw_broken_lines(screen, broken_lines)
            grid.draw_point(screen, points)

        player.draw_player(screen, player_pos[0], player_pos[1])
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
