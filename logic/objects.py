import pygame
from .utils import *


class Player:
    def __init__(self, screen_pos):
        self._scroll = pygame.math.Vector2()
        self.mana = 0
        self.jump_state = False
        self.sprites = {}
        # all sprites that need to be loaded  format [name of file, sprite width]
        temp = {"player": ["player_run", 18]}
        for _, j in enumerate(temp):
            self.sprites[j[0]] = load_animation(j[0], j[1], alpha=True)

        self.rect = self.sprites["player_run"].get_rect(topleft=screen_pos)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.jump_state = True

    def jump(self):
        # do jump stuff
        pass

    @property
    def scroll(self):
        return self._scroll

    def update(self):
        if self.jump_state:
            self.jump()
            self.jump_state = False
