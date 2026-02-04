import pygame
import sys
from settings import *
import grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("PyGame")
    screen.fill(BG_COLOR)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        grid.draw_grid(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
