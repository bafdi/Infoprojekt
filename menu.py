import pygame_menu
from parameter import * # Deine Farben und Größen importieren

# Ein Custom Theme erstellen, das zu deinem Spiel passt
my_theme = pygame_menu.themes.THEME_BLUE.copy()
my_theme.title_font = pygame_menu.font.FONT_FRANCHISE # Oder deine Phosphate Font laden
my_theme.widget_font = pygame_menu.font.FONT_FRANCHISE
my_theme.background_color = BG_COLOR
my_theme.widget_font_color = (0, 0, 0)
my_theme.selection_color = (255, 255, 255) # Highlight Farbe

def start_game():
    # Hier deine Game-Loop Logik aufrufen
    # Wichtig: pygame-menu übernimmt den Loop, bis du das Menü deaktivierst
    pass

menu = pygame_menu.Menu('THE GRID', screen_size, screen_size, theme=my_theme)

menu.add.button('Start Game', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)