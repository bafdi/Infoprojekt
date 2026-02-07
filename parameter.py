#"sizes"
screen_size = 800
grid_dim = 5
broken_lines_qty = 2 ** (grid_dim - 1)
cell_size = screen_size // grid_dim
margin = (screen_size - (grid_dim - 1) * cell_size) // 2
player_size = 20



#Farben
BG_COLOR = (40, 200, 255)
BG_COLOR_TERMINAL = (20, 100, 255)
LINE_COLOR = (100, 255, 255)
LINE_COLOR_SHADE = (50, 125, 125)
LINE_COLOR_TERMINAL = (50, 125, 255)
LINE_COLOR_TERMINAL_SHADE = (100, 200, 255)
PLAYER_COLOR = (255, 255, 255)
BROKEN_COLOR = BG_COLOR
BROKEN_LINE_COLOR = (150, 150, 150)
BROKEN_LINE_COLOR_SHADE = (100, 100, 100)

