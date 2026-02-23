import pygame
from parameter import ENEMY_COLOR


class Enemy:
    """A patrolling enemy that moves along one axis and bounces off walls/broken lines."""

    def __init__(self, x, y, axis, direction=1):
        self.x = x
        self.y = y
        self.axis = axis        # 'h' = horizontal, 'v' = vertical
        self.direction = direction  # +1 or -1

    def move(self, broken_lines, grid_dim):
        if self.axis == 'h':
            nx, ny = self.x + self.direction, self.y
        else:
            nx, ny = self.x, self.y + self.direction

        # Bounce at grid boundaries
        if nx < 0 or nx >= grid_dim or ny < 0 or ny >= grid_dim:
            self.direction *= -1
            return

        # Bounce at broken lines (blocked edges)
        wall = tuple(sorted(((self.x, self.y), (nx, ny))))
        if wall in broken_lines:
            self.direction *= -1
            return

        self.x, self.y = nx, ny


def draw_enemy(screen, enemy, params):
    cell_size = params['cell_size']
    margin = params['margin']
    size = max(10, cell_size // 5)
    px = margin + enemy.x * cell_size
    py = margin + enemy.y * cell_size
    rect = pygame.Rect(px - size // 2, py - size // 2, size, size)
    pygame.draw.rect(screen, ENEMY_COLOR, rect)
    pygame.draw.rect(screen, (140, 0, 0), rect, 2)
