#"sizes"
screen_size = 800
grid_dim = 5
broken_lines_qty = (grid_dim*3)/2
cell_size = screen_size // grid_dim
margin = (screen_size - (grid_dim - 1) * cell_size) // 2
player_size = 20
point_radius = 8
point_qty = 3
header_size = (margin//3)*2
footer_size = (margin//3)
menu_header_size = header_size * 2
menu_text_size = max(16, screen_size // 15)
min_required_moves = (grid_dim - 1) * 2

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


