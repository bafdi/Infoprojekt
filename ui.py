import pygame
import player
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

def draw_won(screen, player_path, score):
    screen.fill(WIN_BG_COLOR)
    player.draw_terminal_line(screen, player_path, color=(0, 140, 0))

    font = pygame.font.SysFont("phosphate", header_size)
    score_text = font.render(f"SCORE: {score}", True, SCHWARZ)
    screen.blit(score_text, [(screen_size//2 - (score_text.get_width()//2)), 10])

    pygame.display.flip()
    pygame.time.wait(3500)


def draw_lost(screen, player_path, score):
    screen.fill(LOSE_BG_COLOR)
    player.draw_terminal_line(screen, player_path, color=(140, 0, 0))

    font = pygame.font.SysFont("phosphate", header_size)
    score_text = font.render(f"SCORE: {score}", True, SCHWARZ)
    screen.blit(score_text, [(screen_size // 2 - (score_text.get_width() // 2)), 10])

    pygame.display.flip()
    pygame.time.wait(2000)