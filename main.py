import pygame
import sys
import grid
import player
import control
from parameter import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("PyGame")
    screen.fill(BG_COLOR)
    clock = pygame.time.Clock()
    player_pos = [0, 2]
    terminal_mode = False

    while True:
        player_pos, terminal_mode = control.handle_input(player_pos, terminal_mode)
        if terminal_mode:
            grid.draw_terminal_grid(screen)
        else:
            grid.draw_grid(screen)

        player.draw_player(screen, player_pos[0], player_pos[1])
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
