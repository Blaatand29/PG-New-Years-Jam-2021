import pygame
from .utils import *
from .map import *
from .background import *
from .config import *
from .objects import *

pygame.init()
CLOCK = Clock()
SCREEN = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.SCALED)

tilemap = TileMap("prototype", "sprites/tilemap")

SCROLL = pygame.math.Vector2(0, 0)

background = Background()


def main():
    dt = 1
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_RETURN:
                    pass
                    # slow_mo()

        SCREEN.fill("black")
        # SCREEN.blit(tilemap, (0, 0))
        background.update(dt)
        background.draw(SCREEN)
        tilemap.draw_map(SCREEN, pygame.Vector2(0, 0) + SCROLL)
        CLOCK.show(SCREEN)
        pygame.display.update()
        CLOCK.update(events)
        dt = CLOCK.dt
