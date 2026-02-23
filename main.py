# pip install pygame pygame-menu

import sys
import pygame_menu
import pygame
import grid
import player
import control
import map_algo
import entity
import ui
import score
from particles import ParticleSystem
from parameter import (BG_COLOR, PLAYER_COLOR, screen_size,
                       menu_header_size, menu_text_size, compute_level_params)


def _spawn_point_particles(particle_system, player_path, points, params):
    """Trigger confetti at each gathered-point position."""
    cell_size = params['cell_size']
    margin = params['margin']
    path_lines = set()
    for i in range(len(player_path) - 1):
        path_lines.add(tuple(sorted((player_path[i], player_path[i + 1]))))
    for pt in points:
        if pt in path_lines:
            (x1, y1), (x2, y2) = pt
            mx = int(((x1 + x2) * cell_size) / 2 + margin)
            my = int(((y1 + y2) * cell_size) / 2 + margin)
            particle_system.add_particles(mx, my)


def _draw_game(screen, game_state, broken_lines, points, teleporters, enemies,
               player_pos, player_path, particle_system, params, remaining_moves):
    """Render one complete game frame (non-menu)."""
    if game_state["terminal_mode"]:
        grid.draw_terminal_grid(screen, params)
        player.draw_terminal_line(screen, player_path, PLAYER_COLOR, params)
    else:
        grid.draw_grid(screen, broken_lines, params)
        grid.draw_broken_lines(screen, broken_lines, params)
        grid.draw_point(screen, points, params)
        grid.draw_teleporters(screen, teleporters, params)

    for e in enemies:
        entity.draw_enemy(screen, e, params)

    particle_system.update()
    particle_system.draw(screen)

    player.draw_player(screen, player_pos[0], player_pos[1], params)
    grid.draw_start_end(screen, params)
    ui.draw_hud(screen, game_state["terminal_mode"], params, remaining_moves)


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("THE GRID")
    screen.fill(BG_COLOR)
    clock = pygame.time.Clock()

    current_level = 1
    params = compute_level_params(current_level)
    game_score = 0

    game_state = {
        "menu_mode": True,
        "terminal_mode": False
    }

    player_pos = [0, 0]
    player_path = [(0, 0)]

    broken_lines = map_algo.generate_broken_lines(params)
    points = map_algo.generate_points(broken_lines, params)
    enemies = map_algo.generate_enemies(params, broken_lines)
    teleporters = map_algo.generate_teleporters(params, broken_lines)

    particle_system = ParticleSystem()
    enemy_move_timer = 0
    enemy_move_interval = 30   # move enemies every 0.5 s at 60 FPS

    remaining_moves = params['max_moves']

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
        nonlocal player_pos, player_path, broken_lines, points, enemies, teleporters, remaining_moves
        player_pos, player_path, broken_lines, points = control.start_new_game(params)
        enemies = map_algo.generate_enemies(params, broken_lines)
        teleporters = map_algo.generate_teleporters(params, broken_lines)
        remaining_moves = params['max_moves']
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
            (player_pos, game_state["terminal_mode"], check,
             game_state["menu_mode"], remaining_moves) = control.handle_input(
                player_pos, game_state["terminal_mode"], broken_lines,
                player_path, game_state["menu_mode"],
                params, teleporters, remaining_moves)

            # Move enemies periodically
            enemy_move_timer += 1
            if enemy_move_timer >= enemy_move_interval:
                enemy_move_timer = 0
                for e in enemies:
                    e.move(broken_lines, params['grid_dim'])

            # Enemy collision check (normal mode)
            if not game_state["terminal_mode"]:
                for e in enemies:
                    if (e.x, e.y) == tuple(player_pos):
                        check = True   # treat as a lost attempt

            if check:
                has_won = control.check_win(player_pos, player_path, broken_lines, params)

                if has_won:
                    game_score += 250
                    gathered_points = score.get_new_score(player_path, points)
                    game_score += gathered_points * 50

                    # Spawn particles at gathered-point positions
                    _spawn_point_particles(particle_system, player_path, points, params)

                    # Brief particle animation before the win screen
                    anim_frames = 0
                    while not particle_system.is_empty() and anim_frames < 90:
                        _draw_game(screen, game_state, broken_lines, points,
                                   teleporters, enemies, player_pos, player_path,
                                   particle_system, params, remaining_moves)
                        pygame.display.flip()
                        clock.tick(60)
                        anim_frames += 1

                    ui.draw_won(screen, player_path, game_score, params)
                    game_state["terminal_mode"] = False

                    # Advance to the next level
                    current_level += 1
                    params = compute_level_params(current_level)
                    player_pos, player_path, broken_lines, points = control.start_new_game(params)
                    enemies = map_algo.generate_enemies(params, broken_lines)
                    teleporters = map_algo.generate_teleporters(params, broken_lines)
                    remaining_moves = params['max_moves']
                    particle_system = ParticleSystem()

                else:
                    game_score -= 100
                    if game_score < 0:
                        game_score = 0
                    ui.draw_lost(screen, player_path, game_score, params)
                    game_state["terminal_mode"] = False
                    player_pos = [0, 0]
                    player_path = [(0, 0)]
                    remaining_moves = params['max_moves']

            if not game_state["terminal_mode"]:
                player_path.clear()
                player_path.append(tuple(player_pos))

            _draw_game(screen, game_state, broken_lines, points,
                       teleporters, enemies, player_pos, player_path,
                       particle_system, params, remaining_moves)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

