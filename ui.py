import pygame
import player
from parameter import SCHWARZ, screen_size, WIN_BG_COLOR, LOSE_BG_COLOR


def draw_hud(screen, terminal_mode, params, remaining_moves=None):
    header_size = params['header_size']
    footer_size = params['footer_size']
    margin = params['margin']

    ausgabetext = "THE GRID"
    font = pygame.font.SysFont("phosphate", header_size)
    text = font.render(ausgabetext, True, SCHWARZ)
    screen.blit(text, [(screen_size // 2 - (text.get_width() // 2)), 10])

    ausgabetext = "Terminalmode: RETURN"
    font = pygame.font.SysFont("phosphate", footer_size)
    text = font.render(ausgabetext, True, SCHWARZ)
    screen.blit(text, [(screen_size - (text.get_width() + (margin // 4))), (screen_size - text.get_height())])

    ausgabetext = "Steuerung: < - ^ - > - v"
    font = pygame.font.SysFont("phosphate", footer_size)
    text = font.render(ausgabetext, True, SCHWARZ)
    screen.blit(text, [(margin // 4), (screen_size - text.get_height())])

    if terminal_mode and remaining_moves is not None:
        moves_text = f"Verbleibende Züge: {remaining_moves}"
        font = pygame.font.SysFont("phosphate", footer_size)
        text = font.render(moves_text, True, SCHWARZ)
        screen.blit(text, [(screen_size // 2 - text.get_width() // 2), (screen_size - text.get_height())])


def draw_won(screen, player_path, score, params):
    screen.fill(WIN_BG_COLOR)
    player.draw_terminal_line(screen, player_path, color=(0, 140, 0), params=params)

    header_size = params['header_size']
    font = pygame.font.SysFont("phosphate", header_size)
    score_text = font.render(f"SCORE: {score}", True, SCHWARZ)
    screen.blit(score_text, [(screen_size // 2 - (score_text.get_width() // 2)), 10])

    pygame.display.flip()
    pygame.time.wait(3500)


def draw_lost(screen, player_path, score, params):
    screen.fill(LOSE_BG_COLOR)
    player.draw_terminal_line(screen, player_path, color=(140, 0, 0), params=params)

    header_size = params['header_size']
    font = pygame.font.SysFont("phosphate", header_size)
    score_text = font.render(f"SCORE: {score}", True, SCHWARZ)
    screen.blit(score_text, [(screen_size // 2 - (score_text.get_width() // 2)), 10])

    pygame.display.flip()
    pygame.time.wait(2000)