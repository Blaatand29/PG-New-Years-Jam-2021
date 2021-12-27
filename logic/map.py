
__all__ = [
    "TileMap"
]

import pygame
from csv import reader
from .utils import *


class Tile:
    def __init__(self, pos, tile_nr, sprite_sheet, tile_size):

        self.pos = pygame.Vector2(pos[0] * tile_size[0], pos[1] * tile_size[1])

        tiles_on_row = sprite_sheet.get_width() // tile_size[0]
        self.surf = clip(
                         sprite_sheet,
                         (int(tile_nr) % tiles_on_row * tile_size[0],
                          int(tile_nr) // tiles_on_row * tile_size[1]), tile_size
                         )

    def draw(self, surface):
        surface.blit(self.surf, self.pos)

    def get_rect(self):
        rect = self.surf.get_rect()
        rect.topleft = self.pos
        return rect


class TileMap:
    def __init__(self, filename, sprite_sheet, scale=2, tile_size=(16, 16)):
        self.path = filename
        self.sprite_sheet = load_image(sprite_sheet)

        self.sprite_sheet = scale_surf(self.sprite_sheet, scale)

        self.tile_size = (tile_size[0] * scale, tile_size[1] * scale)

        self.tiles = []
        map_ = self.read_csv()
        self.load_tiles(map_)

        map_surface_ = pygame.surface.Surface((len(map_[0]) * self.tile_size[0], len(map_) * self.tile_size[1]))
        self.map_surface = map_surface_.copy()
        self.load_map(map_surface_)
        map_surface_.set_colorkey((255, 0, 0))

        self.map_surface.blit(map_surface_, (0, 0))
        self.map_surface.set_colorkey((0, 0, 0))

        self.rects = [i.get_rect() for i in self.tiles]

    def read_csv(self):
        map_ = []
        with open(ASSETS / ("maps/" + self.path + ".csv")) as data:
            data = reader(data, delimiter=",")
            for row in data:
                map_.append(list(row))
        return map_

    def load_tiles(self, map_):
        y = 0
        for row in map_:
            x = 0
            for tile in row:
                if tile != "-1":
                    self.tiles.append(Tile((x, y), tile, self.sprite_sheet, self.tile_size))
                x += 1
            y += 1

    def load_map(self, map_surface_):
        for tile in self.tiles:
            tile.draw(map_surface_)

    def draw_map(self, surface, pos):
        surface.blit(self.map_surface, pos)

    def get_rects(self):
        return self.rects

    def debug(self, screen, map_pos):
        for i in self.rects:
            pygame.draw.rect(screen, "red", pygame.Rect((pygame.Vector2(map_pos) + pygame.Vector2(i.topleft)),
                             self.tile_size), 1)
