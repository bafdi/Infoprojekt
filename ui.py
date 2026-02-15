import pygame
from parameter import *

def draw_hud(screen, terminal_mode):
    ausgabetext = "THE GRID"
    font = pygame.font.SysFont("phosphate", header_size)
    text = font.render(ausgabetext, True, SCHWARZ)
    screen.blit(text, [(screen_size//2 - (text.get_width()//2)), 10])

    ausgabetext = "Terminalmode: RETURN"
    font = pygame.font.SysFont("phosphate", footer_size)
    text = font.render(ausgabetext, True, SCHWARZ)
    screen.blit(text, [(screen_size - (text.get_width() + (margin//4))), (screen_size - text.get_height())])

    ausgabetext = "Steuerung: < - ^ - > - v"
    font = pygame.font.SysFont("phosphate", footer_size)
    text = font.render(ausgabetext, True, SCHWARZ)
    screen.blit(text, [(margin//4), (screen_size - text.get_height())])

