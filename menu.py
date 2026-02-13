import pygame
import sys
from parameter import *

pygame.font.init()
objects = []

class Button():
    def __init__(self, x, y, width, height, buttontext, onclickFuntion = None, onePress = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttontext = buttontext
        self.onclickFuntion = onclickFuntion
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#0c96c4',
            'hover': '#64ffff',
            'pressed': '#00e6e6'
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        font = pygame.font.SysFont('phosphate', menu_text_size)
        self.buttonSurf = font.render(self.buttontext, True, self.fillColors['normal'])

        objects.append(self)

    def process(self, screen):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])

        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFuntion()

                elif not self.alreadyPressed:
                    self.onclickFuntion()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf,
        [self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
                self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2])

        screen.blit(self.buttonSurface, self.buttonRect )

def draw_menu(screen):
    screen.fill(BG_COLOR)




