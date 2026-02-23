import pygame
from parameter import *

def draw_hud(screen, terminal_mode, moves=0, elapsed=0, difficulty='medium'):
    font_large = pygame.font.SysFont("phosphate", header_size)
    font_small = pygame.font.SysFont("phosphate", footer_size)

    # Titel
    title = font_large.render("THE GRID", True, SCHWARZ)
    screen.blit(title, [screen_size // 2 - title.get_width() // 2, 10])

    # Schwierigkeit (oben links)
    diff_label = DIFFICULTY_SETTINGS.get(difficulty, {}).get('label', '')
    diff_surf = font_small.render(diff_label, True, SCHWARZ)
    screen.blit(diff_surf, [margin // 4, 10])

    # Timer (oben rechts)
    secs_total = elapsed // 1000
    mins = secs_total // 60
    secs = secs_total % 60
    timer_surf = font_small.render(f"{mins:02d}:{secs:02d}", True, SCHWARZ)
    screen.blit(timer_surf, [screen_size - timer_surf.get_width() - margin // 4, 10])

    # Modus-Anzeige (oben rechts, zweite Zeile)
    mode_text = "TERMINAL" if terminal_mode else "NORMAL"
    mode_color = (20, 20, 200) if terminal_mode else (0, 80, 0)
    mode_surf = font_small.render(f"Modus: {mode_text}", True, mode_color)
    screen.blit(mode_surf, [screen_size - mode_surf.get_width() - margin // 4, 10 + timer_surf.get_height() + 2])

    # Steuerung (unten links)
    ctrl_surf = font_small.render("Steuerung: WASD / Pfeiltasten", True, SCHWARZ)
    screen.blit(ctrl_surf, [margin // 4, screen_size - ctrl_surf.get_height()])

    # Terminal-Taste (unten rechts)
    term_surf = font_small.render("Terminalmode: RETURN", True, SCHWARZ)
    screen.blit(term_surf, [screen_size - term_surf.get_width() - margin // 4, screen_size - term_surf.get_height()])

    # Zugzähler (unten Mitte) – nur im Terminal-Modus
    if terminal_mode and moves > 0:
        moves_surf = font_small.render(f"Züge: {moves}", True, (20, 20, 200))
        screen.blit(moves_surf, [screen_size // 2 - moves_surf.get_width() // 2, screen_size - moves_surf.get_height()])

