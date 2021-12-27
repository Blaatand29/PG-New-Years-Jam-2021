import pygame
from random import randint, random
from math import sin, cos, radians
from .config import *
from .utils import clamp


class Shape:
    def __init__(self, x=None, y=None, side=0):
        if x is None:
            x = randint(0, screen_width)
        if y is None:
            y = screen_height + 50
        self._x = x
        self._y = y
        self._sides = side
        self._points = []
        self._angle = 0
        self._angle_rate = clamp(random() * 2, 0.2, 2)
        self._size = randint(10, 50)
        angle = radians(360 / side)
        for i in range(side):
            self._points.append(pygame.Vector2(cos(i * angle), sin(i * angle)))

    def update(self, dt):
        self._y += -clamp(self._angle_rate, 0, 1) * dt
        if self._y < -self._size + 10:
            self._y = screen_height + self._size + 10
            self.__init__(side=self._sides)
        self._angle += self._angle_rate * dt

    def draw(self, surf: pygame.Surface):
        points = [i.rotate(self._angle) * self._size for i in self._points]
        for i in points:
            i.update(i.x + self._x, i.y + self._y)
        pygame.draw.polygon(surf, (255, 255, 255), points, 1)


class BaseBackground:
    def __init__(self, color):
        self._paused = False
        self._color = color

    def update(self, dt):
        if self._paused:
            return

    def draw(self, surf: pygame.Surface):
        surf.fill(self._color)


class SquareBackground(BaseBackground):
    def __init__(self, color):
        super().__init__(color)
        self._squares = []
        for _ in range(10):
            self._squares.append(Shape(side=5))

    def update(self, dt):
        super().update(dt)
        for i in self._squares:
            i.update(dt)

    def draw(self, surf: pygame.Surface):
        super().draw(surf)
        for i in self._squares:
            i.draw(surf)


class Background:
    def __init__(self):
        self.background = SquareBackground(color=(0, 0, 55))

    def update(self, dt):
        self.background.update(dt)

    def draw(self, surf):
        self.background.draw(surf)
