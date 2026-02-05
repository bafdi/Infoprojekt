import pygame
import sys
from settings import *
import grid
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("PyGame")
    screen.fill(BG_COLOR)
    clock = pygame.time.Clock()
    player_pos = [0, 2]
    terminal_mode = False

    while True:
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
                    if player_pos[0] < 4:
                        player_pos[0] += 1

                if event.key == pygame.K_a:
                    if player_pos[1] > 0:
                        player_pos[1] -= 1

                if event.key == pygame.K_d:
                    if player_pos[1] < 4:
                        player_pos[1] += 1


        if terminal_mode:
            grid.draw_terminal_grid(screen)
        else:
            grid.draw_grid(screen)

        player.draw_player(screen, player_pos[0], player_pos[1])
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
