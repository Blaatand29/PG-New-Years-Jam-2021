import pygame
from .utils import *
from .map import *
# from .objects import *

pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((320, 180), pygame.FULLSCREEN | pygame.SCALED)

tilemap = TileMap("prototype", "sprites/tilemap")
# player = Player

state = "game"


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit
        
        SCREEN.fill("black")
        tilemap.draw_map(SCREEN, (0, 0))
        # tilemap.debug(SCREEN, (0, 0))
        
        pygame.display.update()
        CLOCK.tick(60)
