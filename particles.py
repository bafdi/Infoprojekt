import pygame
import random
import math


class _Particle:
    __slots__ = ('x', 'y', 'vx', 'vy', 'lifetime', 'max_lifetime', 'color', 'radius')

    def __init__(self, x, y):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1.5, 4.5)
        self.x = float(x)
        self.y = float(y)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.lifetime = random.randint(35, 65)
        self.max_lifetime = self.lifetime
        colors = [
            (255, 255, 0), (255, 165, 0), (255, 80, 80),
            (80, 255, 80), (80, 150, 255), (255, 255, 255),
        ]
        self.color = random.choice(colors)
        self.radius = random.randint(2, 5)


class ParticleSystem:
    def __init__(self):
        self._particles = []

    def add_particles(self, x, y, count=18):
        for _ in range(count):
            self._particles.append(_Particle(x, y))

    def update(self):
        alive = []
        for p in self._particles:
            p.x += p.vx
            p.y += p.vy
            p.vy += 0.12   # gentle gravity
            p.lifetime -= 1
            if p.lifetime > 0:
                alive.append(p)
        self._particles = alive

    def draw(self, screen):
        for p in self._particles:
            fade = p.lifetime / p.max_lifetime
            r, g, b = p.color
            color = (int(r * fade), int(g * fade), int(b * fade))
            pygame.draw.circle(screen, color, (int(p.x), int(p.y)), p.radius)

    def is_empty(self):
        return len(self._particles) == 0
