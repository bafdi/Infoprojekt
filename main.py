# pip install pygame pygame-menu

import sys
import pygame_menu
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

    game_state = {
        "menu_mode": True,
        "terminal_mode": False
    }

    player_pos = [0, 0]
    player_path = [(0, 0)]

    broken_lines = map_algo.generate_broken_lines()
    points = map_algo.generate_points(broken_lines)
    print(broken_lines)
    print(cell_size)
    print(points)

    my_theme = pygame_menu.themes.THEME_BLUE.copy()
    my_theme.background_color = BG_COLOR
    my_theme.title_background_color = (20, 100, 255)

    phosphate_font_path = pygame.font.match_font('phosphate')
    my_theme.title_font = phosphate_font_path
    my_theme.widget_font = phosphate_font_path
    my_theme.title_font_size = menu_header_size
    my_theme.widget_font_size = menu_text_size

    my_theme.widget_font_color = (0, 0, 0)

    def start_game():
        game_state["menu_mode"] = False

    def restart_game():
        nonlocal player_pos, player_path, broken_lines, points
        player_pos, player_path, broken_lines, points = control.start_new_game()
        game_state["menu_mode"] = False

    menu = pygame_menu.Menu('THE GRID', screen_size, screen_size, theme=my_theme)

    menu.add.button('START/Fortsetzen', start_game)
    menu.add.button('LEVEL NEU GENERIEREN', restart_game)
    menu.add.button('BEENDEN', pygame_menu.events.EXIT)


    while True:

        if game_state["menu_mode"]:
            events = pygame.event.get()
            menu.update(events)
            menu.draw(screen)

        else:
            player_pos, game_state["terminal_mode"], check, game_state["menu_mode"] = (
                control.handle_input(player_pos, game_state["terminal_mode"], broken_lines, player_path, game_state["menu_mode"]))

            if check:
                has_won = control.check_win(player_pos, player_path, broken_lines, points)

                if has_won:
                    control.draw_won(screen, player_path)
                    game_state["terminal_mode"] = False
                    player_pos, player_path, broken_lines, points = control.start_new_game()

                else:
                    control.draw_lost(screen, player_path)
                    game_state["terminal_mode"] = False
                    player_pos = [0, 0]
                    player_path = [(0, 0)]

            if game_state["terminal_mode"]:
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
            ui.draw_hud(screen, game_state["terminal_mode"])
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
