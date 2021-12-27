import pygame
from .utils import text


class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.target_fps = 60
        self._dt = 1
        self._slow_mo = False

    @property
    def dt(self):
        return self._dt * self.target_fps

    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_f:
                    if self.fps == 0:
                        self.fps = 60
                    else:
                        self.fps = 0
                if e.key == pygame.K_RETURN:
                    self._slow_mo = not self._slow_mo
        if self._slow_mo:
            self.target_fps -= 1
            if self.target_fps < 10:
                self.target_fps = 10
        else:
            self.target_fps += 1
            if self.target_fps > 60:
                self.target_fps = 60
        self._dt = self.clock.tick(self.fps) / 1000

    def show(self, surf: pygame.Surface):
        surf.blit(text(str(int(self.target_fps))), (0, 0))
