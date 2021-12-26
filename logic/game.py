import pygame
from .utils import *
from .map import *

pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((640, 360), pygame.FULLSCREEN | pygame.SCALED)

tilemap = TileMap("prototype", "sprites/tilemap")

SCROLL = pygame.math.Vector2(0, 0)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        
        SCREEN.fill("black")
        # SCREEN.blit(tilemap, (0, 0))
        tilemap.draw_map(SCREEN, (0, 0) + SCROLL)
        
        pygame.display.update()
        CLOCK.tick(60)
