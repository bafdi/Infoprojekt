#"sizes"
screen_size = 800
player_size = 20
point_radius = 8
point_qty = 3
menu_header_size = 104
menu_text_size = max(16, screen_size // 15)

#Farben
BG_COLOR = (40, 200, 255)
BG_COLOR_TERMINAL = (20, 100, 255)
LINE_COLOR = (100, 255, 255)
LINE_COLOR_SHADE = (50, 125, 125)
LINE_COLOR_TERMINAL = (50, 125, 255)
LINE_COLOR_TERMINAL_SHADE = (100, 200, 255)
PLAYER_COLOR = (255, 255, 255)
POINT_COLOR = (255, 0, 0)
BROKEN_COLOR = BG_COLOR
BROKEN_LINE_COLOR = (150, 150, 150)
BROKEN_LINE_COLOR_SHADE = (100, 100, 100)
HOME_COLOR = (50,50,50)
WIN_BG_COLOR = (0,255,0)
LOSE_BG_COLOR = (255,0,0)
SCHWARZ = (0,0,0)
TELEPORTER_COLOR = (255, 215, 0)
ENEMY_COLOR = (220, 50, 50)


def compute_level_params(level):
    """Return a dict of geometry/gameplay params for the given level number."""
    grid_dim = 4 + level          # Level 1 → 5x5, Level 2 → 6x6, …
    broken_lines_qty = int((grid_dim * 3) / 2)
    cell_size = screen_size // grid_dim
    margin = (screen_size - (grid_dim - 1) * cell_size) // 2
    header_size = max(14, (margin // 3) * 2)
    footer_size = max(10, margin // 3)
    min_required_moves = (grid_dim - 1) * 2
    max_moves = min_required_moves + 5
    return {
        'grid_dim': grid_dim,
        'broken_lines_qty': broken_lines_qty,
        'cell_size': cell_size,
        'margin': margin,
        'header_size': header_size,
        'footer_size': footer_size,
        'min_required_moves': min_required_moves,
        'max_moves': max_moves,
    }


